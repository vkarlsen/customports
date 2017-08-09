--- src/share/poudriere/include/colors.sh.orig	2017-08-09 13:17:19 UTC
+++ src/share/poudriere/include/colors.sh
@@ -77,6 +77,10 @@ if [ ${USE_COLORS} = "no" ]; then
 	COLOR_FAIL=
 	COLOR_PHASE=
 	COLOR_DRY_MODE=
+	COLOR_DELETE_PKG=
+	COLOR_DELETE_PKG_NEW=
+	COLOR_DELETE_PKG_NEWDEP=
+	COLOR_DELETE_PKG_OPTS=
 else
 
 	: ${D_LEFT:="${COLOR_BOLD}[${COLOR_RESET}"}
@@ -92,6 +96,10 @@ else
 	: ${COLOR_FAIL:=${COLOR_RED}}
 	: ${COLOR_PHASE:=${COLOR_LIGHT_MAGENTA}}
 	: ${COLOR_DRY_MODE:=${COLOR_GREEN}}
+	: ${COLOR_DELETE_PKG:=${COLOR_RED}}
+	: ${COLOR_DELETE_PKG_NEW:=${COLOR_GREEN}}
+	: ${COLOR_DELETE_PKG_NEWDEP:=${COLOR_LIGHT_GREEN}}
+	: ${COLOR_DELETE_PKG_OPTS:=${COLOR_YELLOW}}
 fi
 
 colorize_job_id() {
