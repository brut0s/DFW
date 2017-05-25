#!/usr/bin/python

import dox-clear

#HTML

profile = raw_input("Give the Profile a Name: 'Enter CASE:ID/NAME-OF-TARGET': \n>")
print "\nCurrent Working Directory: %s" % os.getcwd()
#save_to_file = raw_input("Please Specify Location to Save Profile: ")

def wrapStringInHTML(firefox, url, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    profilename = profile + '.html'
    f = open(profile,'w')

    doxhtml = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body>
    </html>"""

    whole = wrapper % (program, now, url, body)
    f.write(whole)
    f.close()

    open_new_tab(profile)

