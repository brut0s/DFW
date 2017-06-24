#!/bin/usr/python

import doxclear

#
#
# Basic Info
#
print """\n\t'BASIC-INFO'
\n
\nEnter 'N/A' If It Doesn't Apply
"""
ssn = raw_input("\nEnter the Target's 'SSN-#', like this 999-99-999: \n\n>")
phonenumber = raw_input("\nEnter the Target's 'Phone-Number', like this (999)999-9999: \n\n>")
firstname = raw_input("\nEnter the Target's 'FIRST NAME': \n\n>")
middlename = raw_input("\nEnter the Target's 'MIDDLE NAME': \n\n>")
lastname = raw_input("\nEnter the Target's 'LAST NAME': \n\n>")
ethnicity = raw_input("\nEnter the Target's 'Ethnicity': \n\n>")
religion = raw_input("\nEnter the Target's 'RELIGION': \n\n>")
age = raw_input("\nEnter the Target's 'AGE': \n\n>")
dobm = raw_input("\nEnter the Target's 'MONTH-OF-BIRTH': \n\n>")
dobd = raw_input("\nEnter the Target's 'DAY-OF-BIRTH': \n\n>")
doby = raw_input("\nEnter the Target's 'YEAR-OF-BIRTH': \n\n>")
highschool = raw_input("\nEnter the Name of the 'SCHOOL' where the Target Went to: \n\n>")
highschooladdr = raw_input("\nEnter the Target's 'SCHOOL-STREET-ADDRESS': \n\n>")
highschooltown = raw_input("\nEnter the 'Town' Where the School is: ")
highschoolstate = raw_input("\nEnter the 'State' Where the School is: \n\n>")
highschoolzip = raw_input("\nEnter the Target's 'SCHOOL-AREA-CODE': \n\n>")
highschoolnumber = raw_input("\nEnter the Target's 'SCHOOL-PHONE-NUMBER': \n\n>")
highschoolemail = raw_input("\nEnter the Target's 'SCHOOL-EMAIL-ADDRESS': \n\n>")
highschoolgrad = raw_input("\nEnter the Target's 'Graduation YEAR': \n\n>")
jobplace = raw_input("\nWhere Does the Target 'WORK'? \n\n>")
jobposition = raw_input("\nEnter the Target's job 'POSITION': \n\n>")
workaddr = raw_input("\nEnter the Target's WORK-STREET-ADDRESS': \n\n>")
worktown = raw_input("\nEnter The 'Town' Where the Target Worked: \n\n>")
workstate = raw_input("\nEnter the 'State' Where the Target Worked In: \n\n")
workzip = raw_input("\nEnter the Target's 'WORK-AREA-CODE': \n\n>")
workphone = raw_input("\nEnter the Target's 'WORK-PHONE-NUMBER': \n\n>")
workemail = raw_input("\nEnter the 'EMAIL' Where the Target Works: \n\n>")

doxclear.clear()

#
# Locations
#
print """\n\t'LOCATIONS'
\n
\nEnter 'N/A' If It Doesn't Apply
"""
currentcountry = raw_input("\nEnter the Target's Current 'COUNTRY': \n\n>")
currentstate = raw_input("\nEnter the Target's Current 'STATE/TERRITORY/PROVINCE': \n\n>")
currenttown = raw_input("\nEnter the Target's Current 'TOWN/CITY': \n\n>")
currentzip = raw_input("\nEnter the Target's Current 'ZIP-CODE': \n\n>")
currentstreetaddr = raw_input("\nEnter the Target's Current 'STREET-ADDRESS': \n\n>")
pastcountry = raw_input("\nEnter the Target's Past 'COUNTRY': \n\n>")
paststate = raw_input("\nEnter the Target's Past 'STATE/TERRITORY/PROVINCE': \n\n>")
pasttown = raw_input("\nEnter the Target's Past 'TOWN/CITY': \n\n>")
pastzip = raw_input("\nEnter the Target's Past 'ZIP-CODE': \n\n>")
paststreetaddr = raw_input("\nEnter the Target's Past 'STREET-ADDRESS': \n\n>")

doxclear.clear()

#
#Relationships
#
print "\n\t'RELATIONSHIPS'"
print "\nEnter N/A if it Doesn't Apply"

girlfriend = raw_input("\nEnter the Target's 'GIRL-FRIEND/FIANCE/WIFE' Name: \n\n>")
mother = raw_input("\nEnter the Target's 'MOTHER'S' NAME': \n\n>")
father = raw_input("\nEnter the TArget's 'FATHER'S' Name: \n\n>")

doxclear.clear()

#
# Accounts
#
print """\n\t'ACCOUNTS'
\nEnter 'N/A' If It Doesn't Apply
\nIf Credential's Do Apply Enter It In Like the Following:
\nUser-Name:[testing@yahoo.com]-Password:[test1234]"""

aol = raw_input("\nEnter the Target's 'AOL' Credentals: \n\n>")
outlook = raw_input("\nEnter the Target's 'OUTLOOK' Credentials: \n\n>")
gmail = raw_input("\nEnter the Target's 'GMAIL' Credentials: \n\n>")
yahoo = raw_input("\nEnter the Target's 'YAHOO' Credentials: \n\n>")
facebooklink = raw_input("\nEnter the Target's 'FACEBOOK-PROFILE-URL': \n\n>")
facebook = raw_input("\nEnter the Target's 'FACEBOOK' Credentials: \n\n>")
twitterlink = raw_input("\nEnter the Target's 'TWITTER-PROFILE-URL': \n\n>")
twitter = raw_input("\nEnter the Target's 'TWITTER' Crendtials: \n\n>")
linkedinurl = raw_input("\nEnter the Target's LINKEDIN-PROFILE-URL': \n\n>")
linkedin = raw_input("\nEnter the Target's 'LINKEDIN' Credentials: \n\n>")

doxclear.clear()

#
#Sources
#
print """\n\t'SOURCES'
\nEnter 'N/A' If It Doesn't Apply
"""
sources = raw_input("\nEnter Any Sources about The Target\nif Any at the Prompt \n\nSources:\n\n ")

doxclear.clear()

#
#Summary/Notes
#
print """\n\t'SUMMARY/NOTES'
\nEnter 'N/A' If It Doesn't Apply
"""
notes = raw_input("\nEnter Any Additional Info About the Target if Any at the Prompt \n\nNotes:\n\n ")

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


print ""
doxprofile = raw_input("\nGive the Dox File a Name, \nPreferably with Target's First and Last Name-Dox-Profile.txt\n\n>")
doxfile = open(doxprofile, 'w')

doxfile.write("[+] Basic Info")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t-> Social Security Number:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + ssn)
doxfile.write("\n\n")
doxfile.write("\t-> Phone-Number:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + phonenumber)
doxfile.write("\n\n")
doxfile.write("\t-> First Name:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + firstname)
doxfile.write("\n\n")
doxfile.write("\t-> Middle Name:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + middlename)
doxfile.write("\n\n")
doxfile.write("\t-> Last Name:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + lastname)
doxfile.write("\n\n")
doxfile.write("\t-> Ethnicity:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + ethnicity)
doxfile.write("\n\n")
doxfile.write("\t-> Religion:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + religion)
doxfile.write("\n\n")
doxfile.write("\t-> Age:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + age)
doxfile.write("\n\n")
doxfile.write("\t-> Date Of Birth")
doxfile.write("\n\n")
doxfile.write("\t\t-> Month:" + dobm)
doxfile.write("\n\n")
doxfile.write("\t\t-> Day:" + dobd)
doxfile.write("\n\n")
doxfile.write("\t\t-> Year:" + doby)
doxfile.write("\n\n")
doxfile.write("\t-> High School:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + highschool)
doxfile.write("\n\n")
doxfile.write("\t\t-> Street Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschooladdr)
doxfile.write("\n\n")
doxfile.write("\t\t-> Town/City:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschooltown)
doxfile.write("\n\n")
doxfile.write("\t\t-> State:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschoolstate)
doxfile.write("\n\n")
doxfile.write("\t\t-> Zip Code:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschoolzip)
doxfile.write("\n\n")
doxfile.write("\t\t-> Phone-Number:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschoolnumber)
doxfile.write("\n\n")
doxfile.write("\t\t-> Email-Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschoolemail)
doxfile.write("\n\n")
doxfile.write("\t\t-> Graduation Year:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + highschoolgrad)
doxfile.write("\n\n")
doxfile.write("\t-> Work:")
doxfile.write("\n\n")
doxfile.write("\t\t-> Company:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + jobplace)
doxfile.write("\n\n")
doxfile.write("\t\t-> Positiion:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + jobposition)
doxfile.write("\n\n")
doxfile.write("\t\t-> Street Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + workaddr)
doxfile.write("\n\n")
doxfile.write("\t\t-> Town/City:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + worktown)
doxfile.write("\n\n")
doxfile.write("\t\t-> State:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + workstate)
doxfile.write("\n\n")
doxfile.write("\t\t-> Zip Code:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + workzip)
doxfile.write("\n\n")
doxfile.write("\t\t-> Phone-Number:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + workphone)
doxfile.write("\n\n")
doxfile.write("\t\t-> Email-Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + workemail)
doxfile.write("\n\n")
doxfile.write("[+] Locations")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t-> Current")
doxfile.write("\n\n")
doxfile.write("\t\t-> Country:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + currentcountry)
doxfile.write("\n\n")
doxfile.write("\t\t-> State:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + currentstate)
doxfile.write("\n\n")
doxfile.write("\t\t-> Town/City:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + currenttown)
doxfile.write("\n\n")
doxfile.write("\t\t-> Zip Code:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + currentzip)
doxfile.write("\n\n")
doxfile.write("\t\t-> Street Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + currentstreetaddr)
doxfile.write("\n\n")
doxfile.write("\t-> Past")
doxfile.write("\n\n")
doxfile.write("\t\t-> Country:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + pastcountry)
doxfile.write("\n\n")
doxfile.write("\t\t-> State:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + paststate)
doxfile.write("\n\n")
doxfile.write("\t\t-> Town/City:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + pasttown)
doxfile.write("\n\n")
doxfile.write("\t\t-> Zip Code:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + pastzip)
doxfile.write("\n\n")
doxfile.write("\t\t-> Street Address:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + paststreetaddr)
doxfile.write("\n\n")
doxfile.write("[+] Relationships")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t-> Girlfriend/Wirfe/Fiance:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + girlfriend)
doxfile.write("\n\n")
doxfile.write("\t-> Mother:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + mother)
doxfile.write("\n\n")
doxfile.write("\t-> Father:")
doxfile.write("\n\n")
doxfile.write("\t\t->" + father)
doxfile.write("\n\n")
doxfile.write("[+] Accounts")
doxfile.write("\n")
doxfile.write("-" * 80)
doxfile.write("\n")
doxfile.write("\n")
doxfile.write("\t\t-> AOL:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + aol)
doxfile.write("\n\n")
doxfile.write("\t\t-> OutLook:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + outlook)
doxfile.write("\n\n")
doxfile.write("\t\t-> Gmail:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + gmail)
doxfile.write("\n\n")
doxfile.write("\t\t-> Yahoo:")
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + yahoo)
doxfile.write("\n\n")
doxfile.write("\t\t-> Facebook:")
doxfile.write("\n\n")
doxfile.write("\t\t\t-> Facebook Profile URL" + facebooklink)
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + facebook)
doxfile.write("\n\n")
doxfile.write("\t\t->Twitter:")
doxfile.write("\n\n")
doxfile.write("\t\t\t-> Twitter Profile URL" + twitterlink)
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + twitter)
doxfile.write("\n\n")
doxfile.write("\t\t-> Linked:")
doxfile.write("\n\n")
doxfile.write("\t\t\t-> Linkedin Profile URL" + linkedinurl)
doxfile.write("\n\n")
doxfile.write("\t\t\t->" + linkedin)
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
