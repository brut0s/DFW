#!/usr/bin/python

import os
import doxclear

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

version 1.2017
______________________________________________________________________________________________________________________________

Supports the Following Output Format Only: Text
Future Versions will have: html,pdf

 {{Author}}
***brut0s***

"""

def print_menu():
    print 30 * "-" , "Doxing-Menu" , 30 * "-"
    print "[1]. Create a Profile about a Person"
    print "[2]. Create a Profile for a Company"
    print "[3]. Exit Doxing-Framework"
    print 67 * "-"

loop=True

while loop:
    print_menu()
    choice = input("Select From One of the Fallowing [1-3]: ")

    if choice==1:

	doxclear.clear()
	import personaldox
	doxclear.clear()

    elif choice==2:

        doxclear.clear()
	import companydox
	doxclear.clear()


    elif choice==3:

	print "\nThanks for Using Doxing-FrameWork"
        loop=False

    else:

        raw_input("\n[!]-Error That was a invalid Number, Select from [1-3]")
