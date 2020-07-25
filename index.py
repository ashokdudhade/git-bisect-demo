#!/usr/bin/python

import sys, getopt

def _importfile(arg):
   print 'Import commit 2'

def _exportfile(arg):
   print 'Export commit 3'


def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:e:",["ifile=","efile="])
   except getopt.GetoptError:
      print 'index.py -i <importfile> -e <export file>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'index.py -i <import file> -e <export file>'
         sys.exit()
      elif opt in ("-i", "--import"):
         _importfile(arg)
      elif opt in ("-e", "--export"):
         _exportfile(arg)

if __name__ == "__main__":
   main(sys.argv[1:])