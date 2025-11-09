import pyodbc 
#import sqlalchemy as sa
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
server = "SIDNEGI\\SQLEXPRESS"
database = "NorthWind"
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
#query = "SELECT concat(datepart(year,GETDATE()),'-',datepart(month,GETDATE()),'-',datepart(day,GETDATE())) curr_date;"
query = "SELECT top 1 JobStatus from dbo.ETL_Job_Runs order by JobStatus asc;"
#FAIL status will come before SUCCESS status.
connection = engine.raw_connection();
cursor = connection.cursor();
df = pd.read_sql(query, engine);
print (df);
for index, row in df.iterrows():
    if row.JobStatus == 'FAIL':
        with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/status.txt', 'w') as f:
            print("FAIL", file=f);
    else:
        with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/status.txt', 'w') as f:
            print("CONTINUE", file=f);
#            print("CONTINUE");
    print ("Procedure Successful");
cursor.commit();
cursor.close();