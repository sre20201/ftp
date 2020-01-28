#!/usr/bin/env python 
import codecs
import sys 
import os 
from ftplib import FTP 

PROD="/apps/splunk-data-store/scstarlogs/scstarlogs-prod/"
DR="/apps/splunk-data-store/scstarlogs/scstarlogs-dr/"

def dl_from_ftpprod_dec(): 
  try:
    ftp = FTP(host='10.193.49.86') 
	ftp.login(user = 'ftp.scstar', passwd = 'HtNw7mM2K') 
	ftp.cwd('$sys1.security') 
  except: 
	print 'Unable to FTP 10.193.49.86'
	sys.exit(1) 
	
  f = open('/tmp/files', 'r')
  for opfile in f.readlines():  
    opfile = opfile.strip()
	target = PROD + opfile 
	with codecs.open(target, 'w') as localfile3: 
	  def end13(line): 
	    localfile3.write(line + '\n') 
      ftp.retrlines('RETR' + opfile, end13) 
	  statinfo = os.stat(target) 
	  size = statinfo.st_size 
	  print "op file downloaded as %s with size %d bytes" % (target, size)
	  
  ftp.quit()	
	
def dl_from_ftpdr_dec(): 
  try:
    ftp = FTP(host='10.193.49.107') 
	ftp.login(user = 'ftp.scstar', passwd = 'tandem77') 
	ftp.cwd('$sys1.security') 
  except: 
	print 'Unable to FTP 10.193.49.86'
	sys.exit(1) 
	
  f = open('/tmp/files', 'r')
  for opfile in f.readlines():  
    opfile = opfile.strip()
	target = DR + opfile 
	with codecs.open(target, 'w') as localfile3: 
	  def end13(line): 
	    localfile3.write(line + '\n') 
      ftp.retrlines('RETR' + opfile, end13) 
	  statinfo = os.stat(target) 
	  size = statinfo.st_size 
	  print "op file downloaded as %s with size %d bytes" % (target, size)
	
  ftp.quit() 
   
   
def main():
   dl_from_ftpprod_dec() 
   dl_from_ftpdr_dec()

if __name__ == '__main__':
  main() 
  
