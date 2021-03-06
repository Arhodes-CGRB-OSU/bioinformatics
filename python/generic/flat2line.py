#!/usr/bin/python

import os, sys     # low level handling, such as command line stuff
import string      # string methods available
import getopt      # comand line argument handling
from collections import defaultdict
from low import *  # custom functions, written by myself

# =============================================================================  
def show_help( ):
  """ displays the program parameter list and usage information """
  stdout( "usage: " + sys.argv[0] + " -f <path>" )
  stdout( " " )
  stdout( " option    description" )
  stdout( " -h        help (this text here)" )
  stdout( " -f        flat file to import" )
  stdout( " -d        delimiter (default: ', ' | allowed: any string, tab, space" )
  stdout( " " )
  sys.exit(1)

# =============================================================================
def handle_arguments():
  """ verifies the presence of all necessary arguments and returns the data dir """
  if len ( sys.argv ) == 1:
    stderr( "no arguments provided." )
    show_help()  
  
  try: # check for the right arguments
    keys, values = getopt.getopt( sys.argv[1:], "hf:p:d:" )
  except getopt.GetoptError:
    stderr( "invalid arguments provided." )
    show_help()

  args = {}
  for key, value in keys:
    if key == '-f': args['file'] = value
    if key == '-d': args['delimiter'] = value
    
  if not args.has_key('file'):
    stderr( "import file argument missing." )
    show_help()
  elif not file_exists( args.get('file') ):
    stderr( "import file does not exist." )
    show_help()
    
  if not args.has_key('delimiter'): # or args.get('delimiter') not in [ ";", ",", "tab", "space" ]: 
    args['delimiter'] = ', '
  elif args['delimiter'] == "tab": args['delimiter'] = "\t"
  elif args['delimiter'] == "space": args['delimiter'] = " "

  return args


# =============================================================================
# === MAIN ====================================================================
# =============================================================================
def main( args ):

  hash = defaultdict(list)
  fo = open( args.get('file') )
  for line in fo:
    line = line.rstrip()
    key, value = line.split("\t")
    hash[key].append(value)
  fo.close()
  
  for key, values in hash.iteritems():
    print key + "\t" + string.join(values, args.get('delimiter'))

# =============================================================================
args = handle_arguments()
main( args )

