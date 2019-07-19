--- packet.c.orig	2019-04-17 22:52:57 UTC
+++ packet.c
@@ -93,6 +93,7 @@
 #include "packet.h"
 #include "ssherr.h"
 #include "sshbuf.h"
+#include "blacklist_client.h"
 
 #ifdef PACKET_DEBUG
 #define DBG(x) x
@@ -1841,6 +1842,7 @@ sshpkt_vfatal(struct ssh *ssh, int r, const char *fmt,
 	case SSH_ERR_NO_KEX_ALG_MATCH:
 	case SSH_ERR_NO_HOSTKEY_ALG_MATCH:
 		if (ssh && ssh->kex && ssh->kex->failed_choice) {
+            BLACKLIST_NOTIFY(BLACKLIST_AUTH_FAIL, "ssh");
 			ssh_packet_clear_keys(ssh);
 			logdie("Unable to negotiate with %s: %s. "
 			    "Their offer: %s", remote_id, ssh_err(r),
