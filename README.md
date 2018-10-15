This code is used to configure a remote Cisco device via telnet<br>
Specifically this code changes the VLAN of a device from<br>
a VLAN that has no internet access to one that does. <br>
This code changes the VLAN from whatever it was to VLAN10 <br>
assuming the previous VLAN had no internet access and VLAN 10 does.<br>
You can change the VLAN ID to whatever works for you,<br>
for example if the VLAN that has internet access in your environment is VLAN 50<br>
just change VLAN10 -> VLAN 50<br>
so the code change for the above example would look like this <br>
tn.write("switchport access vlan 50\n")
