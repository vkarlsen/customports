--- src/res.c.orig	2017-06-12 09:29:08 UTC
+++ src/res.c
@@ -563,8 +563,7 @@ res_retrieve_file (const char *url, char
     }
   else
     {
-      err = retrieve_url (url_parsed, robots_url, file, NULL, NULL, NULL,
-                          false, i, false);
+      err = URLERROR;
       url_free(url_parsed);
     }
 
