#This code is used to configure a remote Cisco device
#Specifically this code changes the vlan of a device from 
#a VLAN that has no internet access to one that does 
#this code changes the VLAN from whatever it was to VLAN10
 
import getpass
import telnetlib
import sys

HOST= "10.1.0.2"
user = "test"
password = "test"

tn = telnetlib.Telnet(HOST)

tn.read.until("Username: ")
tn.write(user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

tn.write("en\n")
tn.write("conf t\n")
tn.write("int range gig 1/0/1 - 10\n")
tn.write("switchport access vlan 10\n")
tn.write("end\n")
tn.write("exit\n")
print tn.read_all() 
