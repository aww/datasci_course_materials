
import os

keyfilepath = os.path.expanduser('~/private/twitter_keys.py')
try:
  with open(keyfilepath) as kf:
    exec(kf)
except:
  print "Error: Failed to load keyfile", keyfilepath
  exit()

