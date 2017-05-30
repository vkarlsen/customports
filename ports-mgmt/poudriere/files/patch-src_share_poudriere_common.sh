--- src/share/poudriere/common.sh.orig	2017-05-30 17:47:06 UTC
+++ src/share/poudriere/common.sh
@@ -2403,7 +2403,7 @@ _real_build_port() {
 			JUSER=root
 			;;
 		extract)
-			max_execution_time=3600
+			max_execution_time=14400
 			chown -R ${JUSER} ${mnt}/wrkdirs
 			;;
 		configure) [ -n "${PORTTESTING}" ] && markfs prebuild ${mnt} ;;
@@ -2424,7 +2424,7 @@ _real_build_port() {
 		checksum|*-depends|install-mtree) JUSER=root ;;
 		stage) [ -n "${PORTTESTING}" ] && markfs prestage ${mnt} ;;
 		install)
-			max_execution_time=3600
+			max_execution_time=14400
 			JUSER=root
 			[ -n "${PORTTESTING}" ] && markfs preinst ${mnt}
 			;;
@@ -2443,7 +2443,7 @@ _real_build_port() {
 			fi
 			;;
 		deinstall)
-			max_execution_time=3600
+			max_execution_time=14400
 			JUSER=root
 			# Skip for all linux ports, they are not safe
 			if [ "${PKGNAME%%*linux*}" != "" ]; then
