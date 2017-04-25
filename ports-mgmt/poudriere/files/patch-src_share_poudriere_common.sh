--- src/share/poudriere/common.sh.orig	2017-04-25 18:24:59 UTC
+++ src/share/poudriere/common.sh
@@ -2398,7 +2398,7 @@ _real_build_port() {
 			JUSER=root
 			;;
 		extract)
-			max_execution_time=3600
+			max_execution_time=14400
 			chown -R ${JUSER} ${mnt}/wrkdirs
 			;;
 		configure) [ -n "${PORTTESTING}" ] && markfs prebuild ${mnt} ;;
@@ -2419,12 +2419,12 @@ _real_build_port() {
 		checksum|*-depends|install-mtree) JUSER=root ;;
 		stage) [ -n "${PORTTESTING}" ] && markfs prestage ${mnt} ;;
 		install)
-			max_execution_time=3600
+			max_execution_time=14400
 			JUSER=root
 			[ -n "${PORTTESTING}" ] && markfs preinst ${mnt}
 			;;
 		package)
-			max_execution_time=3600
+			max_execution_time=14400
 			if [ -n "${PORTTESTING}" ] &&
 			    [ -z "${no_stage}" ]; then
 				check_fs_violation ${mnt} prestage "${port}" \
@@ -2438,7 +2438,7 @@ _real_build_port() {
 			fi
 			;;
 		deinstall)
-			max_execution_time=3600
+			max_execution_time=14400
 			JUSER=root
 			# Skip for all linux ports, they are not safe
 			if [ "${PKGNAME%%*linux*}" != "" ]; then
