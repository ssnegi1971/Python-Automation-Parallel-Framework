import sys
import threading
import subprocess
import os

#This is the main file for Python Automation Parallel Framework.
#It invokes the python automation script.
#Multiple data files containing python jobs can be passed as a parameter.
#Also multiple Main processes can be run for multiple sets of jobs each example different warehouses.

def run_script(script_name, param1, param2):
    subprocess.run(["python", script_name, param1, param2]);

if __name__ == "__main__":
    script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/SQLAlchemyPandasPythonProcedureFetchJobs.py","","",));
    script_thread1.start();
    script_thread1.join();
    script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonAutomationJobs.py","C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonJobs.txt","",));
    script_thread1.start();
    script_thread1.join();
    os.remove("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/pythonJobs.txt");
    script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/SQLAlchemyPandasPythonProcedureCheckStatus.py","","",));
    script_thread1.start();
    script_thread1.join();
    with open('C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/status.txt', 'r') as file:
        file_content = file.read().rstrip('\n');
        print(file_content);
        if file_content == 'CONTINUE':
            print("Next Task");
            # Send email configuring your SMTP server.
            script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/sendmailoutlook.py","ssnegi@yahoo.com","Success",));
            script_thread1.start();
            script_thread1.join();
            print ("email sent");
        else:
            print("Failure in Load");
            # Send email configuring your SMTP server.
            script_thread1 = threading.Thread(target=run_script, args=("C:/Users/ssneg/OneDrive/Desktop/work/Python/PythonAutomation/sendmailoutlook.py","ssnegi@yahoo.com","Failure",));
            script_thread1.start();
            script_thread1.join();
            print ("email sent");
            sys.exit(1);
    print("second set of jobs to run");
print("Main script run");