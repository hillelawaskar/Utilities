import subprocess
import os
version = '0.4.0'
package = 'm2x-mqtt'
bin_path = ('C:\ProgramData\Anaconda3\envs\pandas_cub\Scripts')
environment = os.environ.copy()
environment['PATH'] = os.pathsep.join([bin_path, environment['PATH']])

Output = ""
Error = ""

try:
    #passing the env actually creates installs the package in the Virtual env , like I did , else if you dont pass it will install in base environment
    Output = subprocess.check_output("pip install m2x-mqtt==0.4.0",stderr = subprocess.STDOUT,env=environment,shell='True')
    #subprocess.check_call("pip install m2x-mqtt=0.4.0", env=environment, shell=True)
except subprocess.CalledProcessError as e:
    Error =  e.output 
except OSError:
    print("HA_OS_001:OS Error Occurred")
    
    
    
#if Output:
#    Stdout = str(Output.split("\n"))
#else:
#    Stdout = []
#if Error:
#    Stderr = Error.split("\n")
#else:
#    Stderr = []
        
 




####### We need to convert the above code to Function now 


import subprocess
def systemCommand(Command):
    Output = ""
    Error = ""     
    try:
        Output = subprocess.check_output(Command,stderr = subprocess.STDOUT,shell='True')
    except subprocess.CalledProcessError as e:
        Error =  e.output 
    except OSError:
        print("HA_OS_001: OS Error Occurred")
        
    if Output:
        Stdout = Output.split("\n")
    else:
        Stdout = []
    if Error:
        Stderr = Error.split("\n")
    else:
        Stderr = []
    return (Stdout,Stderr)
