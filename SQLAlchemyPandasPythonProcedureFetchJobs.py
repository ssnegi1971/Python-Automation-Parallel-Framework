import pyodbc 
#import sqlalchemy as sa
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import sys
noofjobs=sys.argv[1];
server = "SIDNEGI\\SQLEXPRESS"
database = "NorthWind"
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
query = "SELECT top "+ noofjobs + " jobname from dbo.etl_job_runs where jobstatus in ('Ready','Fail') and joborder = (select min(joborder) from dbo.etl_job_runs where jobstatus in ('Ready','Fail'));"
connection = engine.raw_connection()
cursor = connection.cursor()
df = pd.read_sql(query, engine);
#print (df);
lines = [];
for index, row in df.iterrows():
    lines.append(row.jobname+"\n");
print(lines);
with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonJobs.txt', 'w') as f:
    f.writelines(lines);
    print("null", file=f);
cursor.commit();
cursor.close();
#query = "SELECT * from dbo.grade;"
#df = pd.read_sql(query, engine);
#print (df);
