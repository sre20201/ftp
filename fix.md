<pre>
[root@linuxtutor1232c ~]# cat ftp.py
#!/usr/bin/env python
import codecs
import sys
import os
from ftplib import FTP

PROD="/apps/splunk-data-store/scstarlogs/scstarlogs-prod/"

def dl_from_ftpprod_dec():
  try:
    ftp = FTP(host='127.0.0.1')
    ftp.login(user = 'testuser', passwd = 'india123')
    ftp.cwd('ftp/upload')
  except:
    print 'Unable to FTP 127.0.0.1'
    sys.exit(1)

  f = open('/tmp/files', 'r')
  for opfile in f.readlines():
    opfile = opfile.strip()
    target = PROD + opfile
    with codecs.open(target, 'w') as localfile3:
      def end13(line):
        localfile3.write(line + '\n')
      ftp.retrlines('RETR ' + opfile, end13) ### missing space after RETR was the issue###
      statinfo = os.stat(target)
      size = statinfo.st_size
      print "op file downloaded as %s with size %d bytes" % (target, size)

  ftp.quit()

def main():
   dl_from_ftpprod_dec()

if __name__ == '__main__':
  main()


[root@linuxtutor1232c ~]# cat /tmp/files
OP121823
[root@linuxtutor1232c ~]# cat /home/testuser/ftp/upload/OP121823
This is OP121823 file
[root@linuxtutor1232c ~]# ./ftp.py
op file downloaded as /apps/splunk-data-store/scstarlogs/scstarlogs-prod/OP121823 with size 22 bytes
[root@linuxtutor1232c ~]# ls -ltr /apps/splunk-data-store/scstarlogs/scstarlogs-prod
total 4
-rw-r--r--. 1 root root 22 Feb 12 14:28 OP121823
[root@linuxtutor1232c ~]# cat /apps/splunk-data-store/scstarlogs/scstarlogs-prod/OP121823
This is OP121823 file
[root@linuxtutor1232c ~]#
</pre>
