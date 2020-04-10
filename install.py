#!/usr/bin/env python

import os

tarfile = "/home/cdsw/cviz.tgz"
tgtdir = "/home/cdsw/cviz"

def run():
  if not os.path.exists(tarfile):
    raise Exception('File %s does not exist' % tarfile)

  if os.path.exists(tgtdir):
    print("Deleting directory %s" % tgtdir)
    ret = os.system("rm -rf %s" % tgtdir)
    if ret != 0:
      raise Exception("Failed to delete directory %s" % tgtdir)

  print("Untar'ing file %s" % tarfile)
  ret = os.system("tar xf " + tarfile)
  if ret != 0:
    raise Exception("Failed to untar file %s" % tarfile)

  print("Deleting tarfile %s" % tarfile)
  os.remove(tarfile)

if __name__ == "__main__":
  run()

