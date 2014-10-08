#!/usr/bin/python

from sys import *

if len(argv) < 3:
    print "Usage: " + argv[0] + " file1 file2"
    print "File1 : main api file (generally the smaller one)"
    print "File2 : the trace with hooks applied file (generally the larger one)"
    exit(0)

file1 = open(argv[1], "r")
file2 = open(argv[2], "r")

line1 = file1.readlines()
line2 = file2.readlines()
buffr = ""

x = 0
y = 0
s = 0
while(x != len(line1)):
    if( y == len(line2)):
         j = line1[x].rsplit()
         print "\t Did not find " + j[0] + " at line " + str(x)
         x = x+1
         y = s
         print "...Moving on file1 at line " +str(x) + " and file2 at line " + str(y)
         buffr = ""
    elif(line1[x] == line2[y]):
        if(buffr != ""):
            print buffr
        j = line1[x].rsplit()
        print j[0]
        buffr = ""
        x = x + 1
        y = y + 1
    else:
        if(buffr == ""):
            s = y+1
        j = line2[y].rsplit()
        if(buffr == ""):
            buffr = "\t\t\t" + j[0]
        else:
            buffr = buffr + "\n\t\t\t" + j[0]
        y = y + 1
print buffr
