import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']
    

def create_spark_session():
    """
    create spark session
    """
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    """
    fetch data from S3 and generate songs table and artists table
    write them back to S3
    spark: spark session
    input_data: S3 path of data source
    ourput_Data:destination we write the data after transformation
    """
    # get filepath to song data file
    song_data = ps.path.join(input_data, 'song_data/*/*/*/*.json')
    
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select("song_id", "title", "artist_id","year","duration")
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year","artist").parquest(os.path.join(output_data,'songs.parquest'),'overwrite')

    # extract columns to create artists table
    artists_table = df.select("artist_id", "artist_name", "artist_location", "artist_lattitude", "artist_longitude")
    
    # write artists table to parquet files
    artists_table.write.parquet(os.path.join(output_data, 'artists.parquet'), 'overwrite')


def process_log_data(spark, input_data, output_data):
    """
    fetch data from S3 and generate users table and time table
    generate songplays table by joining two tables
    write them back to S3
    spark: spark session
    input_data: S3 path of data source
    ourput_Data:destination we write the data after transformation
    """
    # get filepath to log data file
    log_data = input_data + 'log_data'

    # read log data file
    df = spark.read.csv(log_data,sep=";", inferSchema=True, header=True)
    
    # filter by actions for song plays
    df = df.where(col("page") == 'NextSong')

    # extract columns for users table    
    user_table = df.select("userId", "firstName", "lastName", "gender", "level")
    
    # write users table to parquet files
    user_table.write.parquet(os.path.join(output_data,'users.parquet'), 'overwrite')

    # create timestamp column from original timestamp column
    get_datetime = udf(lambda x: datetime.fromtimestamp(int(int(x)/1000)), TimestampType())
    get_weekday = udf(lambda x: x.weekday())
    get_week = udf(lambda x: datetime.isocalendar(x)[1])
    get_hour = udf(lambda x: x.hour)
    get_day = udf(lambda x : x.day)
    get_year = udf(lambda x: x.year)
    get_month = udf(lambda x: x.month)
    
   
    df = df.withColumn('start_time', get_datetime(df.ts))
    df = df.withColumn('hour', get_hour(df.start_time))
    df = df.withColumn('day', get_day(df.start_time))
    df = df.withColumn('week', get_week(df.start_time))
    df = df.withColumn('month', get_month(df.start_time))
    df = df.withColumn('year', get_year(df.start_time))
    df = df.withColumn('weekday', get_weekday(df.start_time))

    # extract columns to create time table
    time_table  = df.select('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')    
    
    # write time table to parquet files partitioned by year and month
    time_table.write.parquet(os.path.join(output_data,'time.parquet'), 'overwrite')

    # read in song data to use for songplays table
    song_df = spark.read.parquet("results/songs.parquet")

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = df.join(song_df,(song_df.title == df.song) & (song_df.artist_name == df.artist)).withColumns('songplay_id',monotonically_increasing_id())
    songplays_table = df.select('songplay_id', 'start_time', 'user_id', 'level', 'song_id', 'artist_id', 'session_id', 'location', 'user_agent')


    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year","month").parquet(os.path.join(output_data,'songplays_table.parquet'), 'overwrite')



def main():
    """
    run the process
    """
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "results"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
