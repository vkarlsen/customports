--- servconf.h.orig	2019-04-17 22:52:57 UTC
+++ servconf.h
@@ -210,6 +210,7 @@ typedef struct {
 
 	int	fingerprint_hash;
 	int	expose_userauth_info;
+    int use_blacklist;
 	u_int64_t timing_secret;
 }       ServerOptions;
 
