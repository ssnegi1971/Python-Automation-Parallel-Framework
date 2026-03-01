import pyodbc 
#import sqlalchemy as sa
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
server = "SIDNEGI\\SQLEXPRESS"
database = "NorthWind"
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
query = "SELECT productid from dbo.Products where productname = 'Chai';"
connection = engine.raw_connection()
cursor = connection.cursor()
df = pd.read_sql(query, engine);
#print (df);
for index, row in df.iterrows():
#     cursor.execute("INSERT INTO dbo.dim_client (client_id,created_date,suburb, age) values(?,?,?)", row.client_id, row.created_date, row.suburb, row.age)
#	cursor.execute("update dbo.dim_client set client_id = ?,created_date = ?,suburb = ?, age = ? where client_id = ? and age = ?", 
#		row.client_id, row.created_date, row.suburb, row.age, row.client_id, row.age);
#    cursor.execute("update dbo.student_information set Final_Marks = ? where Student_ID = ?", row.Final_Marks*10, row.Student_ID);
    numpy_int_value = np.int64(row.productid);
    native_int_value = int(numpy_int_value);
    cursor.execute('exec [dbo].[Proc_Products] ?', native_int_value);
    print ("Procedure Successful");
cursor.commit();
cursor.close();
query = "SELECT * from dbo.grade;"
df = pd.read_sql(query, engine);
print (df);