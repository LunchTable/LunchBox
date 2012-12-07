#/usr/bin/python

import tkFileDialog
import json
import os
import sys
from datetime import date
from datetime import datetime

# Helper functions
# Launches a dialog for selecting a file
def open_file():
    filename = tkFileDialog.askopenfilename()
    return filename

# Simplify date from days to years, months, etc.
def simplify_date(days):
	yrs = days / 365
	mos = days % 365 / 30
	days = days % 365 % 30
	
	res = ""
	if (yrs > 0):
		res += "%s year" % yrs
		res += "s " if yrs != 1 else " "
	if (mos > 0):
		res += "%s month" % mos
		res += "s " if mos != 1 else " "
	res += "%s day" % days
	res += "s" if days != 1 else ""
	
	return res
    
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
print "Member for: %s" % simplify_date(delta.days)

# Output other calculated stats
print "Notebook posts: %s" % len(data["notebook"])
print "Sticky notes: %s" % len(data["sticky"])
print

# Calculate last post date
lastPostDate = datetime.fromtimestamp(data["notebook"][0]["posted"]).date()
lastDelta = d0 - lastPostDate
print "Last post %s ago:" % simplify_date(lastDelta.days)
print
print "  \"%s\"" % data["notebook"][0]["value"]

print
