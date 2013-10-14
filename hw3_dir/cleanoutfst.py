#!/opt/python-2.7/bin/python2.7

#Created on 12 Oct, 2013
#authors: Michael Roylance, Olga Whelan


import sys
import re
import os


def main():

  fn1 = sys.argv[1]   # processing the file with best scoring paths 
  f1 = open(fn1, 'ru')

  l = f1.readline()
  while l:
#     print l
    if l[0] = 0:   # but need the other file to extract the string...
      print '=> no'

   ### get the name of the string from fn2
   ### use regex to extract the output sequence
   ### catch the probability in the end of line
   ### address the 0 case


    match = re.search(':\s([\w\"\s]+)\n', l)   # extracting the input string
#    print match
    l = f1.readline()
    l = f1.readline()
    if l[0:5] == "Input":
      print match.group(1), '=> yes'
    else:
      print match.group(1), '=> no' 
      l = f2.readline()

  f2.close()


  
if __name__ == '__main__':
  main()
