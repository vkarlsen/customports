--- serverloop.c.orig	2019-04-17 22:52:57 UTC
+++ serverloop.c
@@ -56,6 +56,8 @@
 #include <unistd.h>
 #include <stdarg.h>
 
+#include <sys/sysctl.h>
+
 #include "openbsd-compat/sys-queue.h"
 #include "xmalloc.h"
 #include "packet.h"
@@ -110,7 +112,19 @@ bind_permitted(int port, uid_t uid)
 {
 	if (use_privsep)
 		return 1; /* allow system to decide */
-	if (port < IPPORT_RESERVED && uid != 0)
+	int ipport_reserved;
+#ifdef __FreeBSD__
+	size_t len_ipport_reserved = sizeof(ipport_reserved);
+
+	if (sysctlbyname("net.inet.ip.portrange.reservedhigh",
+	    &ipport_reserved, &len_ipport_reserved, NULL, 0) != 0)
+		ipport_reserved = IPPORT_RESERVED;
+	else
+		ipport_reserved++;
+#else
+	ipport_reserved = IPPORT_RESERVED;
+#endif
+	if (port < ipport_reserved && uid != 0)
 		return 0;
 	return 1;
 }
