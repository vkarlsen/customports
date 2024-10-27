--- ubsplitmap.py.orig	2020-02-05 22:09:54 UTC
+++ ubsplitmap.py
@@ -5,7 +5,7 @@ for split horizon DNS that would work in a dynamic fas
 for split horizon DNS that would work in a dynamic fashion.
 """
 
-from configparser import SafeConfigParser
+from configparser import ConfigParser
 from fnmatch import fnmatch
 import os, socket
 
@@ -29,7 +29,7 @@ class Globals(object):
     conf = None
 
 
-class MyConfigParser(SafeConfigParser):
+class MyConfigParser(ConfigParser):
     """
     Subclass to make some particular lookups easier
     """
