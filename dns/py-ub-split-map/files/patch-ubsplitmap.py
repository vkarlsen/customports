--- ubsplitmap.py.orig	2017-08-19 23:25:13 UTC
+++ ubsplitmap.py
@@ -10,9 +10,6 @@ from fnmatch import fnmatch
 import os , socket
 
 CONFIG_SEARCH = [
-    '/etc/ub-split-map.ini' ,
-    '/etc/unbound/ub-split-map.ini' ,
-    '/usr/local/etc/ub-split-map.ini' ,
     '/usr/local/etc/unbound/ub-split-map.ini' ,
 ]
 
@@ -22,8 +19,6 @@ if 'HOME' in os.environ:
         os.path.join(os.environ['HOME'] , '/unbound/ub-split-map.ini') ,
     ])
 
-CONFIG_SEARCH.append('/home/jay/sandbox/ub-split-map/ub-split-map.ini')
-
 class Globals(object):
     conf = None
 
