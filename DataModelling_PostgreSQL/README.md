### Introduction
- This project is completed for Startup called 'Sparkify - A music streaming company'. 
- The aim of the project is to create a Postgres database with tables designed to optimize queries on song play analysis. 
- A star schema for database and ETL pipeline for analysis is created using Python3 and SQL
#

### Raw Data
- JSON logs on user activity on the app
- JSON metadata on the songs in the app
#

### PostgreSQL table
- A Fact table of Songs-Played
- Dimenisons Table: Users, Songs, Artists and time 
#

### Project Implementation
#### There are 3 project phases: 
- Database and tables creation
   * Fact and Dimesnions tables are idenitied and created
   - Data Definitions and Constraints are created
   - Create, Insert and Upsert operations are created 
- ETL processes building
   * Extract- Transform Processes are identified in this phase: 
   - Json data is transformed to pandas dataframes
   - Duplicates are removed adhering to table constraints
   - Data is enhanced to meet all requirements set in phase1
   - Data is pushed into SQL tables through post-greSQL connection in Python
   - Testing is done before complete automation
- ETL pipeline building
   * A automated Extract, Transform and Load pipeline is created to rapidly push data into SQL tables
 # 
 
 ### How to run this project
 - Clone the repository
 
 - Change the settings parameters: password and user for accessing PostgreSQL server in settings.py
 
 - Install the requirements using requirements.txt
 
 - Run the files in order from commandline:
      * python3 create_tables.py
      - python3 etl.py
      
      You can view the results in postgreSQL server.
  
      ![](https://github.com/RammySekham/Data-Modelling-ETL/blob/main/DataModelling_PostgreSQL/postgreSQL_database.PNG)
      #
      
      
 - Use codeSample.py to query the data for analysis
   #      
  
