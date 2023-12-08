import subprocess, platform
print(".......Connected Wi-Fi Detailes........")
os_name = platform.system()

if os_name == "Windows":
   list_networks_command = 'netsh wlan show networks'
   output = subprocess.check_output(list_networks_command, shell=True, text=True)
   print(output)
   
elif os_name == "Linux":
   list_networks_command = "nmcli device wifi list"
   output = subprocess.check_output(list_networks_command, shell=True, text=True)
   print(output)
else:  
   print("Unsupported OS")
   
import subprocess
print(".......Wi-Fi Password Detailes........")

command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")




