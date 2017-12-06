--- src/share/poudriere/include/colors.sh.orig	2017-12-06 16:39:36 UTC
+++ src/share/poudriere/include/colors.sh
@@ -79,6 +79,10 @@ if [ ${USE_COLORS} = "no" ]; then
 	COLOR_FAIL=
 	COLOR_PHASE=
 	COLOR_DRY_MODE=
+    COLOR_DELETE_PKG=
+    COLOR_DELETE_PKG_NEW=
+    COLOR_DELETE_PKG_NEWDEP=
+    COLOR_DELETE_PKG_OPTS=
 else
 
 	: ${D_LEFT:="${COLOR_BOLD}[${COLOR_RESET}"}
@@ -95,6 +99,10 @@ else
 	: ${COLOR_FAIL:=${COLOR_RED}}
 	: ${COLOR_PHASE:=${COLOR_LIGHT_MAGENTA}}
 	: ${COLOR_DRY_MODE:=${COLOR_GREEN}}
+    : ${COLOR_DELETE_PKG:=${COLOR_RED}}
+    : ${COLOR_DELETE_PKG_NEW:=${COLOR_GREEN}}
+    : ${COLOR_DELETE_PKG_NEWDEP:=${COLOR_LIGHT_GREEN}}
+    : ${COLOR_DELETE_PKG_OPTS:=${COLOR_YELLOW}}
 fi
 
 colorize_job_id() {
