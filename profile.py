#/usr/bin/python

import tkFileDialog
import json
import os
import sys
from datetime import date

# Helper functions
# Launches a dialog for selecting a file
def open_file():
    filename = tkFileDialog.askopenfilename()
    return filename
    
# Give us a fresh slate to work on
os.system('cls' if os.name=='nt' else 'clear')

print
print "LunchBox v1"
print "--------------------------------------------------------------------------------"
print "select your exported *.json file."

fname = open_file()

if fname == '':
	print "no file selected."
	print
	sys.exit()

json_data = open(fname)

data = json.load(json_data)

json_data.close()

print "opening " + fname + "..."
print 
# End opening logging

# Begin data output
if data["username"]:
	print " " + data["username"]
elif data["realname"]:
	print " " + data["realname"]
else:
	print " No name."
print

# Gender information
if data["gender"] == 'F':
	print "Female"
else:
	print "Male"

# Calculate member duration
dateParts = data["joindate"].split('-')
d0 = date.today()
d1 = date(int(dateParts[0]), int(dateParts[1]), int(dateParts[2]))
delta = d0 - d1

# Output our calculated stats
print "Member for: %s days" % delta.days
print "Notebook posts: %s" % len(data["notebook"])
print "Sticky notes: %s" % len(data["sticky"])

print
