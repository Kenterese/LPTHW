# impoty arguments from the system(terminal) to argv(array list)
from sys import argv
# Importing Framework
script, filename  = argv
#Set Variable, txt
txt = open(filename)

print "Here's your file %r" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()