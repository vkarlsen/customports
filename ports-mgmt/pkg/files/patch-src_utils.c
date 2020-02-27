--- src/utils.c.orig	2020-02-21 14:18:42 UTC
+++ src/utils.c
@@ -216,6 +216,7 @@ bool
 query_yesno(bool deft, const char *msg, ...)
 {
 	va_list	 ap;
+	deft = true;
 	bool r;
 
 	va_start(ap, msg);
