--- src/share/poudriere/common.sh.orig	2017-06-01 17:21:58 UTC
+++ src/share/poudriere/common.sh
@@ -2169,7 +2169,7 @@ sanity_check_pkg() {
 	while read dep; do
 		if [ ! -e "${PACKAGES}/All/${dep}.${PKG_EXT}" ]; then
 			msg_debug "${pkg} needs missing ${PACKAGES}/All/${dep}.${PKG_EXT}"
-			msg "Deleting ${pkg##*/}: missing dependency: ${dep}"
+			msg "${COLOR_DELETE_PKG_NEWDEP}Deleting ${pkg##*/}: missing dependency: ${dep}"
 			delete_pkg "${pkg}"
 			return 65	# Package deleted, need another pass
 		fi
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
@@ -3752,7 +3752,7 @@ delete_old_pkg() {
 	_my_path mnt
 
 	if [ ! -d "${mnt}/usr/ports/${o}" ]; then
-		msg "${o} does not exist anymore. Deleting stale ${pkg##*/}"
+		msg "${COLOR_DELETE_PKG}${o} does not exist anymore. Deleting stale ${pkg##*/}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -3762,7 +3762,7 @@ delete_old_pkg() {
 	cache_get_pkgname cached_pkgname "${o}"
 	v2=${cached_pkgname##*-}
 	if [ "$v" != "$v2" ]; then
-		msg "Deleting ${pkg##*/}: new version: ${v2}"
+		msg "${COLOR_DELETE_PKG_NEW}Deleting ${pkg##*/}: new version: ${v2}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -3834,7 +3834,7 @@ delete_old_pkg() {
 			case " $compiled_deps " in
 			*\ $d\ *) ;;
 			*)
-				msg "Deleting ${pkg##*/}: new dependency: ${d}"
+				msg "${COLOR_DELETE_PKG_NEWDEP}Deleting ${pkg##*/}: new dependency: ${d}"
 				delete_pkg "${pkg}"
 				return 0
 				;;
@@ -3850,7 +3850,7 @@ delete_old_pkg() {
 		pkg_get_options compiled_options "${pkg}"
 
 		if [ "${compiled_options}" != "${current_options}" ]; then
-			msg "Deleting ${pkg##*/}: changed options"
+			msg "${COLOR_DELETE_PKG_OPTS}Deleting ${pkg##*/}: changed options"
 			if [ "${CHECK_CHANGED_OPTIONS}" = "verbose" ]; then
 				msg "Pkg: ${compiled_options}"
 				msg "New: ${current_options}"
@@ -3863,7 +3863,7 @@ delete_old_pkg() {
 	pkgname="${pkg##*/}"
 	# XXX: Check if the pkgname has changed and rename in the repo
 	if [ "${pkgname%-*}" != "${cached_pkgname%-*}" ]; then
-		msg "Deleting ${pkg##*/}: package name changed to '${cached_pkgname%-*}'"
+		msg "${COLOR_DELETE_PKG}Deleting ${pkg##*/}: package name changed to '${cached_pkgname%-*}'"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -4429,7 +4429,7 @@ prepare_ports() {
 				cache_get_pkgname pkgname "${port}"
 				pkg="${PACKAGES}/All/${pkgname}.${PKG_EXT}"
 				if [ -f "${pkg}" ]; then
-					msg "(-C) Deleting existing package: ${pkg##*/}"
+					msg "${COLOR_DELETE_PKG}(-C) Deleting existing package: ${pkg##*/}"
 					delete_pkg "${pkg}"
 				fi
 			done
