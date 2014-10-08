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


x = 0
y = 0
while(x != len(line1)):
    if( y == len(line2)):
         break
    elif(line1[x] == line2[y]):
        j = line1[x].rsplit()
        print j[0]
        x = x + 1
        y = y + 1
    else:
        j = line2[y].rsplit()
        print "\t\t\t" + j[0]
        y = y + 1

