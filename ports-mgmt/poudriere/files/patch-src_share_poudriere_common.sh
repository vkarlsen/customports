--- src/share/poudriere/common.sh.orig	2017-11-11 17:07:32 UTC
+++ src/share/poudriere/common.sh
@@ -2988,7 +2988,7 @@ _real_build_port() {
 			JUSER=root
 			;;
 		extract)
-			max_execution_time=3600
+			max_execution_time=28800
 			if [ "${JUSER}" != "root" ]; then
 				chown -R ${JUSER} ${mnt}/wrkdirs
 			fi
@@ -3012,12 +3012,12 @@ _real_build_port() {
 		checksum|*-depends) JUSER=root ;;
 		stage) [ -n "${PORTTESTING}" ] && markfs prestage ${mnt} ;;
 		install)
-			max_execution_time=3600
+			max_execution_time=28800
 			JUSER=root
 			[ -n "${PORTTESTING}" ] && markfs preinst ${mnt}
 			;;
 		package)
-			max_execution_time=7200
+			max_execution_time=57600
 			if [ -n "${PORTTESTING}" ]; then
 				check_fs_violation ${mnt} prestage \
 				    "${originspec}" \
@@ -3031,7 +3031,7 @@ _real_build_port() {
 			fi
 			;;
 		deinstall)
-			max_execution_time=3600
+			max_execution_time=28800
 			JUSER=root
 			# Skip for all linux ports, they are not safe
 			if [ "${PKGNAME%%*linux*}" != "" ]; then
@@ -4900,7 +4900,7 @@ delete_old_pkg() {
 	_my_path mnt
 
 	if [ ! -d "${mnt}${PORTSDIR}/${origin}" ]; then
-		msg "${origin} does not exist anymore. Deleting stale ${pkg##*/}"
+		msg "${COLOR_DELETE_PKG}${origin} does not exist anymore. Deleting stale ${pkg##*/}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -4937,7 +4937,7 @@ delete_old_pkg() {
 		# with a different origin.  Such as lang/perl5.20 vs
 		# lang/perl5.22 both with 'perl5' as PKGBASE.  A pkgclean
 		# would handle removing this.
-		msg "Deleting ${pkg##*/}: stale package: unwanted origin ${originspec}"
+		msg "${COLOR_DELETE_PKG_NEWDEP}Deleting ${pkg##*/}: stale package: unwanted origin ${originspec}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -4948,14 +4948,14 @@ delete_old_pkg() {
 	# version may show for a stale package that has been renamed.
 	# XXX: Check if the pkgname has changed and rename in the repo
 	if [ "${pkgbase}" != "${new_pkgbase}" ]; then
-		msg "Deleting ${pkg##*/}: package name changed to '${new_pkgbase}'"
+		msg "${COLOR_DELETE_PKG}Deleting ${pkg##*/}: package name changed to '${new_pkgbase}'"
 		delete_pkg "${pkg}"
 		return 0
 	fi
 
 	v2=${new_pkgname##*-}
 	if [ "$v" != "$v2" ]; then
-		msg "Deleting ${pkg##*/}: new version: ${v2}"
+		msg "${COLOR_DELETE_PKG_NEW}Deleting ${pkg##*/}: new version: ${v2}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -5071,7 +5071,7 @@ delete_old_pkg() {
 					*) ;;
 					esac
 				fi
-				msg "Deleting ${pkg##*/}: new dependency: ${d}"
+				msg "${COLOR_DELETE_PKG_NEWDEP}Deleting ${pkg##*/}: new dependency: ${d}"
 				delete_pkg "${pkg}"
 				return 0
 				;;
@@ -5101,7 +5101,7 @@ delete_old_pkg() {
 		pkg_get_options compiled_options "${pkg}"
 
 		if [ "${compiled_options}" != "${current_options}" ]; then
-			msg "Deleting ${pkg##*/}: changed options"
+			msg "${COLOR_DELETE_PKG_OPTS}Deleting ${pkg##*/}: changed options"
 			if [ "${CHECK_CHANGED_OPTIONS}" = "verbose" ]; then
 				msg "Pkg: ${compiled_options}"
 				msg "New: ${current_options}"
@@ -6617,7 +6617,7 @@ prepare_ports() {
 			listed_pkgnames | while read pkgname; do
 				pkg="${PACKAGES}/All/${pkgname}.${PKG_EXT}"
 				if [ -f "${pkg}" ]; then
-					msg "(-C) Deleting existing package: ${pkg##*/}"
+					msg "${COLOR_DELETE_PKG}(-C) Deleting existing package: ${pkg##*/}"
 					delete_pkg_xargs "${delete_pkg_list}" \
 					    "${pkg}"
 				fi
