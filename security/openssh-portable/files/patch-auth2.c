--- auth2.c.orig	2019-04-17 22:52:57 UTC
+++ auth2.c
@@ -49,10 +49,12 @@
 #include "sshkey.h"
 #include "hostfile.h"
 #include "auth.h"
+#include "canohost.h"
 #include "dispatch.h"
 #include "pathnames.h"
 #include "sshbuf.h"
 #include "ssherr.h"
+#include "blacklist_client.h"
 
 #ifdef GSSAPI
 #include "ssh-gss.h"
@@ -268,7 +270,14 @@ input_userauth_request(int type, u_int32_t seq, struct
 	char *user = NULL, *service = NULL, *method = NULL, *style = NULL;
 	int r, authenticated = 0;
 	double tstart = monotime_double();
+#ifdef HAVE_LOGIN_CAP
+	login_cap_t *lc;
+	const char *from_host, *from_ip;
 
+	from_host = auth_get_canonical_hostname(ssh, options.use_dns);
+	from_ip = ssh_remote_ipaddr(ssh);
+#endif
+
 	if (authctxt == NULL)
 		fatal("input_userauth_request: no authctxt");
 
@@ -319,6 +328,27 @@ input_userauth_request(int type, u_int32_t seq, struct
 		    "not allowed: (%s,%s) -> (%s,%s)",
 		    authctxt->user, authctxt->service, user, service);
 	}
+
+#ifdef HAVE_LOGIN_CAP
+	if (authctxt->pw != NULL) {
+		lc = login_getpwclass(authctxt->pw);
+		if (lc == NULL)
+			lc = login_getclassbyname(NULL, authctxt->pw);
+		if (!auth_hostok(lc, from_host, from_ip)) {
+			logit("Denied connection for %.200s from %.200s [%.200s].",
+			    authctxt->pw->pw_name, from_host, from_ip);
+			ssh_packet_disconnect(ssh, "Sorry, you are not allowed to connect.");
+		}
+		if (!auth_timeok(lc, time(NULL))) {
+			logit("LOGIN %.200s REFUSED (TIME) FROM %.200s",
+			    authctxt->pw->pw_name, from_host);
+			ssh_packet_disconnect(ssh, "Logins not available right now.");
+		}
+		login_close(lc);
+		lc = NULL;
+	}
+#endif  /* HAVE_LOGIN_CAP */
+
 	/* reset state */
 	auth2_challenge_stop(ssh);
 
@@ -426,8 +456,10 @@ userauth_finish(struct ssh *ssh, int authenticated, co
 	} else {
 		/* Allow initial try of "none" auth without failure penalty */
 		if (!partial && !authctxt->server_caused_failure &&
-		    (authctxt->attempt > 1 || strcmp(method, "none") != 0))
+		    (authctxt->attempt > 1 || strcmp(method, "none") != 0)) {
 			authctxt->failures++;
+            BLACKLIST_NOTIFY(BLACKLIST_AUTH_FAIL, "ssh");
+        }
 		if (authctxt->failures >= options.max_authtries) {
 #ifdef SSH_AUDIT_EVENTS
 			PRIVSEP(audit_event(ssh, SSH_LOGIN_EXCEED_MAXTRIES));
