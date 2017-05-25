#!/usr/bin/python

import os
#import dox-clear
#import dox-accounts
#import dox-basic-info
#import dox-locations-info
#import dox-relationships-info
#import dox-sources
#import dox-summary
#import dox-html


print """

Welcome to

         .-'```````-.
       .'            `.
      /                \
     ;                 ;`
     |         H       |;
     ;                 ;|
     '\               / ;
      \`.           .' /
       `.`-._____.-' .'
         / /`_____.-'
        / / /
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
 ____            _                   _____                       __        __         _
|  _ \  _____  _(_)_ __   __ _      |  ___| __ __ _ _ __ ___   __\ \      / /__  _ __| | __
| | | |/ _ \ \/ / | '_ \ / _`'|_____| |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| | (_) >  <| | | | | (_| |_____|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
|____/ \___/_/\_\_|_| |_|\__, |     |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
                         |___/
______________________________________________________________________________________________________________________________

[#]...This Program is Designed for Creating Profiles About Your Target
[#]...Doxing-Framework is a Automated Doxing Tool for Creating a Clean, and Readable Profile about the Target
[#]...This Tool has a simple integrated menu With Options for a Dox Template For Doxing a Person, and Info-sec/Recon
[!]...I Do Not Take Responsability for Using This Tool to Aid in Malicous Activity
______________________________________________________________________________________________________________________________

Supports the Following Output Formats: HTML, PDF, and Text

 {{Author}}
***brut0s***

"""

exit = 1
status = 0

while exit == 1:
#os.system("clear")
#if status != 0:

 print "Select from one of the Following Doxing Formats?"
 print "\n[1]. Create a Profile about a Person"
 print "\n[2]. Create a Profile for a Company "
 print "[99]. Exit Doxing-Framework"

option = int(raw_input("Choice: "))


if option == 1:
#os.system("clear")

 print "Now I Need Some Intel About the Person"

	#dox-basic-info()
	#dox-clear()
	#dox-locations-info()
	#dox-relationships-info()
	#dox-accounts-info()
	#dox-summary()

print "Your Profile of the Targeted Person is Complete, would you like to return to the main menu?"
print "1 = Yes"
print "2 = No"
exit = int(raw_input("Choice: "))
else:
status = 0

if option == 99:
exit = 2


if option == 2:
#os.system("clear")
print "Now I Need Some Intel About the Company"

	#dox-clear()
	#dox-locations-info()
	#dox-internet-info()
	#dox-summary()

#os.system("clear")

print "Your Profile of the Targeted Company is Complete, would you like to return to the main menu?"
print "[1] = Yes"
print "[2] = No"
#exit = int(raw_input("Choice: "))
#else:
#status = 0


#os.system("clear")
print "Thank you for using Doxing-Framework"
