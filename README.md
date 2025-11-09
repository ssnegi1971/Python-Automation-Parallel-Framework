# Python-Automation-Parallel-Framework

I have written a Python Automation Parallel Framework.
It consists of the below components:
pythonAutomationJobsMain.py
pythonAutomationJobs.py
pythonJobs.txt

The process flow is as follows:
The pythonAutomationJobsMain.py passes the pythonJobs.txt file as a parameter to pythonAutomationJobs.py.
pythonAutomationJobsMain.py –
extracts the jobs contained in pythonJobs.txt
It runs the job in separate thread processes in parallel.
Each job writes status information to a database status table.
When all the jobs running in parallel have finished it stops.
Then it processes the next jobs file from the Main program.
Multiple Main programs can be invoked for different data sources, example warehouses. 

The complete free source code is available at the link - PythonAutomation

1.	pythonAutomationJobsMain.py

import sys
import threading
import subprocess

#This is the main file for Python Automation Parallel Framework.
#It invokes the python automation script.
#Multiple data files containing python jobs can be passed as a parameter.
#Also multiple Main processes can be run for multiple sets of jobs each example different warehouses.

def run_script(script_name, param):
    subprocess.run(["python", script_name, param]);

if __name__ == "__main__":
    script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonAutomationJobs.py","C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonJobs.txt",));
    script_thread1.start();
    script_thread1.join();
    script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/SQLAlchemyPandasPythonProcedureCheckStatus.py","",));
    script_thread1.start();
    script_thread1.join();
    with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/status.txt', 'r') as file:
        file_content = file.read().rstrip('\n');
        print(file_content);
        if file_content == 'CONTINUE':
            print("Next Task");
        else:
            print("Failure in Load");
            sys.exit(1);
    print("second set of jobs to run");
print("Main script run");

2.	pythonAutomationJobs.py

import sys
import threading
import subprocess

#This is a Python Automation Parallel Framework. It runs python scripts in parallel.
#It is programmed for maximum 5 python jobs in pythonJobs.txt seperated by a comma.
#The sixth or last element is null inserted for collecting the previous subprocesses.
#It can be expanded to more parallel jobs depending on requirement.

file_path=sys.argv[1];

def run_script(script_name):
    subprocess.run(["python", script_name]);
"""
with open(file_path, 'r') as file:
    file_content = file.read();
print (file_content);
split_list = file_content.split(',');
print (split_list);
"""
lines = [];
with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip());
print(lines);
for index, item in enumerate(lines):
    print(f"Index: {index}, Item: {item}")
    if __name__ == "__main__":
        if index == 0 and item != 'null':
            script_thread1 = threading.Thread(target=run_script, args=(item,));
            script_thread1.start();
        elif index == 1 and item != 'null':
            script_thread2 = threading.Thread(target=run_script, args=(item,));
            script_thread2.start();
        elif index == 2 and item != 'null':
            script_thread3 = threading.Thread(target=run_script, args=(item,));
            script_thread3.start();
        elif index == 3 and item != 'null':
            script_thread4 = threading.Thread(target=run_script, args=(item,));
            script_thread4.start();
        elif index == 4 and item != 'null':
            script_thread5 = threading.Thread(target=run_script, args=(item,));
            script_thread5.start();
        elif item == "null":
            if index==1:
                 script_thread1.join();
            elif index == 2:
                script_thread1.join();
                script_thread2.join();
            elif index == 3:
                script_thread1.join();
                script_thread2.join();
                script_thread3.join();
            elif index == 4:
                script_thread1.join();
                script_thread2.join();
                script_thread3.join();
                script_thread4.join();                
            elif index == 5:
                script_thread1.join();
                script_thread2.join();
                script_thread3.join();
                script_thread4.join();
                script_thread5.join();                
            print("All scripts have finished executing.");

3.	pythonJobs.txt
C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/SubProcess1.py
C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/SubProcess2.py
C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/SQLAlchemyPandasPythonProcedure3.py
null
4.	SQLAlchemyPandasPythonProcedureCheckStatus.py

import pyodbc 
#import sqlalchemy as sa
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
server = "SIDNEGI\\SQLEXPRESS"
database = "NorthWind"
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')
query = "SELECT top 1 JobStatus from dbo.ETL_Job_Runs order by JobStatus asc;"
#FAIL status will come before SUCCESS status.
connection = engine.raw_connection()
cursor = connection.cursor()
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

5.	dbo.ETL_Job_Runs
USE [NorthWind]
GO

/****** Object:  Table [dbo].[ETL_Job_Runs]    Script Date: 3/11/2025 11:20:28 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ETL_Job_Runs](
	[SerialNo] [int] IDENTITY(1,1) NOT NULL,
	[JobName] [varchar](40) NULL,
	[RunTime] [datetime] NULL,
	[JobStatus] [varchar](20) NULL,
	[ErrorMsg] [varchar](100)
) ON [PRIMARY]
GO

6.	SubProcess1.py

import subprocess
#This subprocess is not required as the procedure script can be invoked directly from pythonJobs.txt.
subprocess.run(["python","SQLAlchemyPandasPythonProcedure1.py"]);

7.	SQLAlchemyPandasPythonProcedure1.py
# A sample python procedure invocation from the framework.
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
    numpy_int_value = np.int64(row.productid);
    native_int_value = int(numpy_int_value);
    cursor.execute('exec [dbo].[Proc_Products] ?', native_int_value);
    print ("Procedure Successful");
cursor.commit();
cursor.close();

8.	dbo.Proc_Products
USE [NorthWind]
GO

/****** Object:  StoredProcedure [dbo].[Proc_Products]    Script Date: 3/11/2025 4:15:47 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

create procedure [dbo].[Proc_Products] 
	@productid int AS
begin
declare @productname nvarchar(40);
SELECT @productname=productname
FROM products
where productid = @productid
print 'product name ' + @productname
if @productname='Chai'
 print 'country India'
insert into dbo.etl_job_runs values ('Proc_Products', GETDATE(), 'SUCCESS', ‘No Error’);
end;
Go