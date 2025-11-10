import pyodbc 
#import sqlalchemy as sa
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import sys
#noofjobs=sys.argv[1];
server = "SIDNEGI\\SQLEXPRESS"
database = "NorthWind"
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
query = "SELECT top 5 jobname from dbo.etl_job_runs where jobstatus in ('Ready','Fail') and joborder = (select min(joborder) from dbo.etl_job_runs where jobstatus in ('Ready','Fail'));"
connection = engine.raw_connection()
cursor = connection.cursor()
df = pd.read_sql(query, engine);
#print (df);
for index, row in df.iterrows():
    with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonJobs.txt', 'a') as f:
        print(row.jobname, file=f);
cursor.commit();
cursor.close();
query = "SELECT * from dbo.grade;"
df = pd.read_sql(query, engine);
print (df);
