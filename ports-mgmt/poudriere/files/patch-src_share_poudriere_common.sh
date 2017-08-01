--- src/share/poudriere/common.sh.orig	2017-08-01 10:34:16 UTC
+++ src/share/poudriere/common.sh
@@ -2916,7 +2916,7 @@ _real_build_port() {
 			JUSER=root
 			;;
 		extract)
-			max_execution_time=3600
+			max_execution_time=14400
 			if [ "${JUSER}" != "root" ]; then
 				chown -R ${JUSER} ${mnt}/wrkdirs
 			fi
@@ -2939,7 +2939,7 @@ _real_build_port() {
 		checksum|*-depends) JUSER=root ;;
 		stage) [ -n "${PORTTESTING}" ] && markfs prestage ${mnt} ;;
 		install)
-			max_execution_time=3600
+			max_execution_time=14400
 			JUSER=root
 			[ -n "${PORTTESTING}" ] && markfs preinst ${mnt}
 			;;
@@ -2957,7 +2957,7 @@ _real_build_port() {
 			fi
 			;;
 		deinstall)
-			max_execution_time=3600
+			max_execution_time=14400
 			JUSER=root
 			# Skip for all linux ports, they are not safe
 			if [ "${PKGNAME%%*linux*}" != "" ]; then
