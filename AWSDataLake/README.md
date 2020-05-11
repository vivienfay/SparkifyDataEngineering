- The purpose of this project:

Sparkify is a straming music service. This project will be helping Sparkify to design a dimension modelling based on its business, which enable them to improve the data infrastructure for analysis. 

Based on the environment provided by them, the ETL procedure should be designed on the AWS S3 and EMR.

For ETL procedure, firstly we need to fetch data from S3 by spark, and use Spark to reorganize the schema based on our design. After we tranform them as the parquest file, then we are free to save them and write them into S3 back.


- The database schema Design: 

For Sparkify's business, the key business consists of serveral components. Thus, when designing the schema, the archiecture contains 1 fact table and 4 dimension tables. The fact table contains song play acivity of users and dimension tables contain the detailed information of song, artist, time, and user.

- How to run the Python scripts:

    run ETL
    In Python console, use the command: 
    !python etl.py
    
- The explanation of the files in the repository:

    1. dwh.cfg
    
    the configuration file to connect S3. Has AWS access key and secret credentials.

    2. etl.py
    
    For getting data from S3 to Redshift and select the columns we want based on the design using Spark and write them back to S3

    3. Readme.md
    
    Detailed explaination for this project






