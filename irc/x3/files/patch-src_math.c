--- src/math.c.orig	2013-12-17 00:22:19 UTC
+++ src/math.c
@@ -24,12 +24,8 @@
 #include "saxdb.h"
 #include "timeq.h"
 
-#ifndef HAVE_MATH_H
-  #include <math.h>
-  #include <complex.h>
-#else
-  #include <tgmath.h>
-#endif
+#include <math.h>
+#include <complex.h>
 
 #include <ctype.h>
 #include <stdio.h>
