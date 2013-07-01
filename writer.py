#! /usr/bin/python

from sys import stdout

def writer(options):
  if options.write:
    fout = open(options.write, 'w')
    write = fout.write
  else:
    write = stdout.write

  return write
