--- sshconnect.c.orig	2019-04-17 22:52:57 UTC
+++ sshconnect.c
@@ -43,6 +43,7 @@
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
+#include <rpc/rpc.h>
 #include <unistd.h>
 #ifdef HAVE_IFADDRS_H
 # include <ifaddrs.h>
