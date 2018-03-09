--- src/share/poudriere/common.sh.orig	2018-03-09 19:40:50 UTC
+++ src/share/poudriere/common.sh
@@ -7535,10 +7535,10 @@ DRY_RUN=0
 : ${RESOLV_CONF="/etc/resolv.conf"}
 : ${MAX_EXECUTION_TIME:=86400}         # 24 hours for 1 command (phase)
 # Some phases have different timeouts.
-: ${MAX_EXECUTION_TIME_EXTRACT:=3600}
-: ${MAX_EXECUTION_TIME_INSTALL:=3600}
-: ${MAX_EXECUTION_TIME_PACKAGE:=7200}
-: ${MAX_EXECUTION_TIME_DEINSTALL:=3600}
+: ${MAX_EXECUTION_TIME_EXTRACT:=28800}
+: ${MAX_EXECUTION_TIME_INSTALL:=28800}
+: ${MAX_EXECUTION_TIME_PACKAGE:=14400}
+: ${MAX_EXECUTION_TIME_DEINSTALL:=28800}
 : ${NOHANG_TIME:=7200}                 # 120 minutes with no log update
 : ${QEMU_MAX_EXECUTION_TIME:=345600}   # 4 days for 1 command (phase)
 : ${QEMU_NOHANG_TIME:=21600}           # 6 hours with no log update
