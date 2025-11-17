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
query = "SELECT count(serialno) total_cnt, (select count(*) from dbo.etl_job_runs where jobstatus = 'Success') cnt_success from dbo.etl_job_runs;"
connection = engine.raw_connection()
cursor = connection.cursor()
df = pd.read_sql(query, engine);
#print (df);
for index, row in df.iterrows():
    if row.total_cnt != row.cnt_success:
        with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/keepprocessing.txt', 'w') as f:
            print("LOOP", file=f);
    else:
        with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/keepprocessing.txt', 'w') as f:
            print("STOP", file=f);
cursor.commit();
cursor.close();
#query = "SELECT * from dbo.grade;"
#df = pd.read_sql(query, engine);
#print (df);
