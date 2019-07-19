--- auth.c.orig	2019-04-17 22:52:57 UTC
+++ auth.c
@@ -75,6 +75,7 @@
 #include "authfile.h"
 #include "ssherr.h"
 #include "compat.h"
+#include "blacklist_client.h"
 #include "channels.h"
 
 /* import */
@@ -330,8 +331,11 @@ auth_log(struct ssh *ssh, int authenticated, int parti
 		authmsg = "Postponed";
 	else if (partial)
 		authmsg = "Partial";
-	else
+	else {
 		authmsg = authenticated ? "Accepted" : "Failed";
+        if (authenticated)
+            BLACKLIST_NOTIFY(BLACKLIST_AUTH_OK, "ssh");
+    }
 
 	if ((extra = format_method_key(authctxt)) == NULL) {
 		if (authctxt->auth_method_info != NULL)
@@ -599,7 +603,7 @@ getpwnamallow(struct ssh *ssh, const char *user)
 	if (!allowed_user(ssh, pw))
 		return (NULL);
 #ifdef HAVE_LOGIN_CAP
-	if ((lc = login_getclass(pw->pw_class)) == NULL) {
+	if ((lc = login_getpwclass(pw)) == NULL) {
 		debug("unable to get login class: %s", user);
 		return (NULL);
 	}
