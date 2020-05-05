- The purpose of this project:

Sparkify is a straming music service. This project will be helping Sparkify to design a dimension modelling based on its business, which enable them to improve the data infrastructure for analysis. 

For ETL procedure, firstly we created the empty tables based on our schema design for storing the data. Next, from the raw data source, we created insert query to insert the data to those empty tables we created earlier. Keep in mind that load the data in dimension table first and then the data for fact table.

- The database schema Design: 
For Sparkify's business, the key business consists of serveral components such as . Thus, when designing the schema, the archiecture contains 1 fact table and 4 dimension table. The fact table contains song play acivity of users and dimension tables contain the detailed information of song, artist, time, and user.

- How to run the Python scripts:

    1. Create empty tables
    In Python console, use the command: 
    !python create_tables.py

    2. run ETL
    In Python console, use the command: 
    !python etl.py
    
- The explanation of the files in the repository:

    1. folder: data
    
    the raw data source 

    2. create_tables.py
    
    it will connect to the server and the trigger the action to create the tables we designed for the database.

    3. etl.ipynb
    
    Before working on the etl.py, I worked on this to test if every step is correct

    4. Readme.md
    
    Detailed explaination for this project

    5. SQL_queries.py
    
    contains the sql queries which will be used in this project to create tables and insert data.

    6. test.ipynb
    
    for testing. You will see the result returned after your manipulation for the database.




