- The purpose of this project:

Sparkify is a straming music service. This project will be helping Sparkify to design a dimension modelling based on its business, which enable them to improve the data infrastructure for analysis. 

Based on the environment provided by them, the ETL procedure should be designed on the AWS S3 and Redshift.

For ETL procedure, firstly we created the empty tables for staging the raw data and empty tables based on our schema design for storing the data. Next, from the raw data source (S3), we copy the data to staging table in Redshift from S3. Then, we are able to transform the data to the schema we design to the empty fact tables and dimension tables using the insert query.

- The database schema Design: 

For Sparkify's business, the key business consists of serveral components. Thus, when designing the schema, the archiecture contains 1 fact table and 4 dimension tables. The fact table contains song play acivity of users and dimension tables contain the detailed information of song, artist, time, and user.

- How to run the Python scripts:

    1. Create empty tables
    In Python console, use the command: 
    !python create_tables.py

    2. run ETL
    In Python console, use the command: 
    !python etl.py
    
- The explanation of the files in the repository:

    1. dwh.cfg
    
    the configuration file of S3 and Redshift setting information for connecting S3 and Redshift. 

    2. create_tables.py
    
    it will connect to the Redshift and the trigger the action to clear up the tables and create the tables we designed for the database.

    3. etl.py
    
    For copying the data from S3 to Redshift and insert the fact and dimension tables with the transformed data.

    4. Readme.md
    
    Detailed explaination for this project

    5. SQL_queries.py
    
    contains the sql queries which will be used in this project to drop tables, create tables, copy data and insert data.






