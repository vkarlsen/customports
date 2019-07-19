--- sshd.c.orig	2019-07-19 17:59:50 UTC
+++ sshd.c
@@ -46,6 +46,7 @@
 
 #include <sys/types.h>
 #include <sys/ioctl.h>
+#include <sys/mman.h>
 #include <sys/socket.h>
 #ifdef HAVE_SYS_STAT_H
 # include <sys/stat.h>
@@ -85,6 +86,13 @@
 #include <prot.h>
 #endif
 
+#ifdef __FreeBSD__
+#include <resolv.h>
+#ifdef GSSAPI
+#include "ssh-gss.h"
+#endif
+#endif
+
 #include "xmalloc.h"
 #include "ssh.h"
 #include "ssh2.h"
@@ -122,6 +130,7 @@
 #include "auth-options.h"
 #include "version.h"
 #include "ssherr.h"
+#include "blacklist_client.h"
 
 #ifdef LIBWRAP
 #include <tcpd.h>
@@ -376,6 +385,8 @@ grace_alarm_handler(int sig)
 		kill(0, SIGTERM);
 	}
 
+    BLACKLIST_NOTIFY(BLACKLIST_AUTH_FAIL, "ssh");
+
 	/* XXX pre-format ipaddr/port so we don't need to access active_state */
 	/* Log error and exit. */
 	sigdie("Timeout before authentication for %s port %d",
@@ -1905,6 +1916,10 @@ main(int ac, char **av)
 	/* Reinitialize the log (because of the fork above). */
 	log_init(__progname, options.log_level, options.log_facility, log_stderr);
 
+ 	/* Avoid killing the process in high-pressure swapping environments. */
+ 	if (!inetd_flag && madvise(NULL, 0, MADV_PROTECT) != 0)
+ 		debug("madvise(): %.200s", strerror(errno));
+
 	/* Chdir to the root directory so that the current disk can be
 	   unmounted if desired. */
 	if (chdir("/") == -1)
@@ -2020,7 +2035,30 @@ main(int ac, char **av)
 	signal(SIGCHLD, SIG_DFL);
 	signal(SIGINT, SIG_DFL);
 
+#ifdef __FreeBSD__
 	/*
+	 * Initialize the resolver.  This may not happen automatically
+	 * before privsep chroot().
+	 */
+	if ((_res.options & RES_INIT) == 0) {
+		debug("res_init()");
+		res_init();
+	}
+#ifdef GSSAPI
+	/*
+	 * Force GSS-API to parse its configuration and load any
+	 * mechanism plugins.
+	 */
+	{
+		gss_OID_set mechs;
+		OM_uint32 minor_status;
+		gss_indicate_mechs(&minor_status, &mechs);
+		gss_release_oid_set(&minor_status, &mechs);
+	}
+#endif
+#endif
+
+	/*
 	 * Register our connection.  This turns encryption off because we do
 	 * not have a key.
 	 */
@@ -2124,6 +2162,8 @@ main(int ac, char **av)
 	if ((loginmsg = sshbuf_new()) == NULL)
 		fatal("%s: sshbuf_new failed", __func__);
 	auth_debug_reset();
+
+    BLACKLIST_INIT();
 
 	if (use_privsep) {
 		if (privsep_preauth(ssh) == 1)
