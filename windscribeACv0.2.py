import os
import requests
import random
import time
import argparse

print("Welcome to Windscribe VPN Autoconnector v0.2")
print "By @Rag_Sec"
print " "

parser = argparse.ArgumentParser(description='Please choose one of the options')
parser.add_argument('-c','--connect', help='Connect to a random node', action="store_true")
parser.add_argument('-d', '--disconnect', help='Disconnect from windscribe', action="store_true")
parser.add_argument('-n', '--new', help='Change exit node', action="store_true")
parser.add_argument('-s', '--start', help='Start Windscribe Daemon', action="store_true")
args = parser.parse_args()
serverloc =['US-C','Chicago','Dallas','Miami','Vice','House','Los Angeles','Seattle','CA', 'Toronto', 'CA-W', 'Stanley', 'GB', 'FR', 'DE', 'NL', 'NO', 'RO', 'CH', 'GB' , 'Tea', 'HK']

if args.start:
	print("Please enter your superuser password")
 	os.system("sudo systemctl start windscribe")
	print "Sucessfully started Windscribe daemon"

if args.connect:
	os.system("windscribe connect " + random.choice(serverloc))
	print ("VPN connected")
	choice = 1
	while choice == 1:
		change = raw_input("would you like to change node [Y/N]")
		if change == 'Y' or change == 'y':
			os.system("windscribe connect " + random.choice(serverloc))
		else:
			choice = 0
			
if args.disconnect:
	print("Disconnecting")
	os.system("windscribe disconnect")

if args.new:
	os.system("windscribe connect " + random.choice(serverloc))
	choice = 1
	while choice == 1:
		change = raw_input("would you like to change node [Y/N]")
		if change == 'Y' or change == 'y':
			os.system("windscribe connect " + random.choice(serverloc))
		else:
			choice = 0		

print "Thank you for using Windscribe VPN Autoconnector"
