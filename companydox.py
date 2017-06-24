#!/bin/usr/python

import doxclear

#
#
# Company Info
#
print """\n\t'COMPANY-INFO'
\n
\nEnter 'N/A' If It Doesn't Apply
"""
compname = raw_input("\nEnter the Company's 'NAME': \n\n>")
compphone = raw_input("\nEnter the Company's 'Phone-Number', like this (999)999-9999: \n\n>")
compemail = raw_input("\nEnter the Company's 'EMAIL' \n\n>")
compcountry = raw_input("\nEnter the 'COUNTRY' the Company Is In: \n\n>")
compaddr = raw_input("\nEnter the Company's 'STREET-ADDRESS': \n\n>")
comptown = raw_input("\nEnter The 'TOWN' Where the Company Is In: \n\n>")
compstate = raw_input("\nEnter the 'STATE' Where the Company Is Located: \n\n")
compzip = raw_input("\nEnter the Company's 'AREA-CODE': \n\n>")

doxclear.clear()

#
#Internet
#
print """\n\t'INTERNET'
\nEnter 'N/A' If It Doesn't Apply
"""
compsite = raw_input("\nEnter the Company's Website: \n\n>")
hoststate = raw_input("\nEnter the Host's Online State [up/down]: \n\n>")
openports = raw_input("\nEnter any Open Ports On the Host System: \n\n>")
filteredports = raw_input("\nEnter and Filtered Ports On the Host System: \n\n>")
closedports = raw_input("\nEnter any Closed Ports On the Host System: \n\n>")
portsscan = raw_input("\nEnter and Ports You've Scanned: \n\n>")
hostuptime = raw_input("\nEnter the Host's Up Time: \n\n>")
lastboot = raw_input("\nEnter the Host's Last Known Boot: \n\n>")
ipv4 = raw_input("\nEnter the Host's IPV4 Address: \n\n>")
ipv6 = raw_input("\nEnter the Host's IPV6 Address: \n\n>")
mac = raw_input("\nEnter the Host's Mac Address: \n\n")
os = raw_input("\nEnter the Host's Operating System: \n\n>")
acc = raw_input("\nEnter Host's Operating System Guess Accurcy: \n\n>")
portinfo = raw_input("""\nEnter any Running Ports, Port-State and Protocol on the Host System,
\nLike this:
\n\n21-[openssh-server-vs.2.91]-[Open] \n\n>
""")
compsmtp = raw_input("\nEnter the Company's 'SMTP' Server-Address: \n\n>")
compsmtpport = raw_input("\nEnter the Company's 'SMTP-PORT': \n\n>")
osclass = raw_input("\nEnter the Host's Operating System Class: \n\n>")
osvender = raw_input("\nEnter the Host's Operating System Vender [Ubuntu,Microsoft,Mac, etc.]: \n\n>")
osfamily = raw_input("\nEnter the Host's Operating System Family: \n\n>")
osgeneration = raw_input("\nEnter the Host's Operating System Generation: \n\n>")
osgenacc = raw_input("\nEnter Host's Operating System Generation Guess Accurcy: \n\n>")

doxclear.clear()

#
#Sources
#
print """\n\t'SOURCES'
\nEnter 'N/A' If It Doesn't Apply
"""
sources = raw_input("\nEnter Any Sources about the Company at the Prompt \n\nSources:\n\n ")

doxclear.clear()

#
#Summary/Notes
#
print """\n\t'SUMMARY/NOTES'
\nEnter 'N/A' If It Doesn't Apply
"""
notes = raw_input("\nEnter Any Additional Info About the Company if Any at the Prompt \n\nNotes:\n\n ")

doxclear.clear()

#
# Useful Websites
#
print """\n\t'Useful Websites'
\nEnter 'N/A' If It Doesn't Apply
"""
usefulsites = raw_input("\nEnter Any Useful Websites: \n\n ")

doxclear.clear()


#
# This Code Writes the Users
# Input to a Text File
#
# import time
## dd/mm/yyyy format

doxprofile = raw_input("\nGive the Dox File a Name, \nPreferably with with Company's Name-Dox-Profile.txt\n\n>")
doxfile = open(doxprofile, 'w')

doxfile.write("[+] Company Info")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t-> Company Name:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + compname)
doxfile.write("\n\n")
doxfile.write("\t-> Phone-Number:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + compphone)
doxfile.write("\n\n")
doxfile.write("\t-> Email-Address:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + compemail)
doxfile.write("\n\n")
doxfile.write("[+] Location")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t\t-> Country:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + compcountry)
doxfile.write("\n\n")
doxfile.write("\t\t-> State:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + compstate)
doxfile.write("\n\n")
doxfile.write("\t\t-> Town/City:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + comptown)
doxfile.write("\n\n")
doxfile.write("\t\t-> Zip Code:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + compzip)
doxfile.write("\n\n")
doxfile.write("\t\t-> Street Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + compaddr)
doxfile.write("\n\n")
doxfile.write("[+] Internet")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t-> Company Site:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + compsite)
doxfile.write("\n\n")
doxfile.write("\t-> Host State:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + hoststate)
doxfile.write("\n\n")
doxfile.write("\t-> Open Ports:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + openports)
doxfile.write("\n\n")
doxfile.write("\t-> Filtered Ports:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + filteredports)
doxfile.write("\n\n")
doxfile.write("\t-> Closed Ports:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + closedports)
doxfile.write("\n\n")
doxfile.write("\t-> Ports Scanned:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + portsscan)
doxfile.write("\n\n")
doxfile.write("\t-> Uptime:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + hostuptime)
doxfile.write("\n\n")
doxfile.write("\t-> Last Boot:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + lastboot)
doxfile.write("\n\n")
doxfile.write("\t-> Addresses:")
doxfile.write("\n\n")
doxfile.write("\t\t-> SMTP:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + compsmtp)
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + compsmtpport)
doxfile.write("\n\n")
doxfile.write("\t\t-> IPV-4:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + ipv4)
doxfile.write("\n\n")
doxfile.write("\t\t-> IPV-6:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + ipv6)
doxfile.write("\n\n")
doxfile.write("\t\t-> MAC-Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + mac)
doxfile.write("\n\n")
doxfile.write("\t-> Operating System:")
doxfile.write("\n\n")
doxfile.write("\t\t-> Operating System Name:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + os)
doxfile.write("\n\n")
doxfile.write("\t\t-> Accuracy")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + acc)
doxfile.write("\n\n")
doxfile.write("\t-> Ports Used:")
doxfile.write("\n\n")
doxfile.write("\t\t-> Port:Version:State")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + portinfo)
doxfile.write("\n\n")
doxfile.write("\t-> Operating System Class:")
doxfile.write("\n\n")
doxfile.write("\t\t-> Class:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + osclass)
doxfile.write("\n\n")
doxfile.write("\t\t-> OS Vender:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + osvender)
doxfile.write("\n\n")
doxfile.write("\t\t-> OS Family:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + osfamily)
doxfile.write("\n\n")
doxfile.write("\t\t-> OS Generation:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + osgeneration)
doxfile.write("\n\n")
doxfile.write("\t\t-> Accuracy:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + osgenacc)
doxfile.write("\n\n")
doxfile.write("[+] Sources")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t\t->" + sources)
doxfile.write("\n\n")
doxfile.write("[+] Summary")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t\t->" + notes)
doxfile.write("\n\n")
doxfile.close()

print "\n[+]...Dox-Profile Complete"

cont = raw_input("\n[!]...Press 'Return' to Continue")
