--- src/share/poudriere/common.sh.orig	2017-06-01 17:21:58 UTC
+++ src/share/poudriere/common.sh
@@ -2411,7 +2411,7 @@ _real_build_port() {
 			JUSER=root
 			;;
 		extract)
-			max_execution_time=3600
+			max_execution_time=28800
 			chown -R ${JUSER} ${mnt}/wrkdirs
 			;;
 		configure) [ -n "${PORTTESTING}" ] && markfs prebuild ${mnt} ;;
@@ -2432,12 +2432,12 @@ _real_build_port() {
 		checksum|*-depends|install-mtree) JUSER=root ;;
 		stage) [ -n "${PORTTESTING}" ] && markfs prestage ${mnt} ;;
 		install)
-			max_execution_time=3600
+			max_execution_time=28800
 			JUSER=root
 			[ -n "${PORTTESTING}" ] && markfs preinst ${mnt}
 			;;
 		package)
-			max_execution_time=7200
+			max_execution_time=28800
 			if [ -n "${PORTTESTING}" ] &&
 			    [ -z "${no_stage}" ]; then
 				check_fs_violation ${mnt} prestage "${port}" \
@@ -2451,7 +2451,7 @@ _real_build_port() {
 			fi
 			;;
 		deinstall)
-			max_execution_time=3600
+			max_execution_time=28800
 			JUSER=root
 			# Skip for all linux ports, they are not safe
 			if [ "${PKGNAME%%*linux*}" != "" ]; then
