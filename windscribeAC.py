import os
import requests
import random
import time

print("Welcome to Windscribe VPN Autoconnector")
print("Please enter your superuser password")
time.sleep(1)
os.system("sudo systemctl start windscribe")
print "Sucessfully started Windscribe daemon"
serverloc =['London','Frankfurt','Atlanta','Munich','Hong Kong','Zurich','Bucharest','Oslo','Amsterdam','Paris']
os.system("windscribe connect " + random.choice(serverloc))
print ("VPN connected")
disconnect = raw_input("would you like to disconnect [Y/N]")
if disconnect == 'Y' or disconnect == 'y':
	os.system("windscribe disconnect")
	print "Thank you for using Windscribe VPN Autoconnector"
