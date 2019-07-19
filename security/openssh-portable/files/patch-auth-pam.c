--- auth-pam.c.orig	2019-04-17 22:52:57 UTC
+++ auth-pam.c
@@ -103,6 +103,7 @@ extern char *__progname;
 #include "ssh-gss.h"
 #endif
 #include "monitor_wrap.h"
+#include "blacklist_client.h"
 
 extern ServerOptions options;
 extern struct sshbuf *loginmsg;
@@ -900,6 +901,8 @@ sshpam_query(void *ctx, char **name, char **info,
 				free(msg);
 				return (0);
 			}
+            BLACKLIST_NOTIFY(BLACKLIST_BAD_USER,
+                sshpam_authctxt->user);
 			error("PAM: %s for %s%.100s from %.100s", msg,
 			    sshpam_authctxt->valid ? "" : "illegal user ",
 			    sshpam_authctxt->user, sshpam_rhost);
