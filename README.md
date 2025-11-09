# Python-Automation-Parallel-Framework

I have written a Python Automation Parallel Framework.

It consists of the below components:

pythonAutomationJobsMain.py

pythonAutomationJobs.py

pythonJobs.txt

The process flow is as follows:

The pythonAutomationJobsMain.py passes the pythonJobs.txt file as a parameter to pythonAutomationJobs.py.
pythonAutomationJobsMain.py extracts the jobs contained in pythonJobs.txt

It runs the job in separate thread processes in parallel.

Each job writes status information to a database status table.

When all the jobs running in parallel have finished it stops.

Then it processes the next jobs file from the Main program.

Multiple Main programs can be invoked for different data sources, example warehouses. 
