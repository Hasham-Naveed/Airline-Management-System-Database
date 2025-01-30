•	airline-schema png file contains schema diagram of airline management system.

•	airline-basic-tables.sql file contains only those tables defined in schema.

•	airline-additional-tables.sql file contains additional history tables and procedures and triggers.

•	airline-faker.py is used to populate/insert data into database tables.

•	requirements.txt file is used to install libraries used for faker code.

                  INSTALLATION!

                  
•	Run airline-basic-tables.sql file in MS SQL Server after opening it.

•	You can also run airline-additional-tables.sql file to create history tables.


•	You can either run "pip install pyodbc faker" in cmd OR run "pip install -r requirements.txt" in cmd but remember your cmd should be in that directory where your requirements.txt file is.

Before running “airline-faker.py” replace “Server” and “Database” name to your system server name and database name.

[Untitled](https://github.com/user-attachments/assets/2475947f-9394-4642-8aee-32037e689c37)
 
•	Run "airline-faker.py" in cmd but remember your cmd should be in that directory where your airline-faker.py file is.
