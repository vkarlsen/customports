--- src/share/poudriere/common.sh.orig	2017-12-06 16:41:50 UTC
+++ src/share/poudriere/common.sh
@@ -2989,7 +2989,7 @@ _real_build_port() {
 			JUSER=root
 			;;
 		extract)
-			max_execution_time=3600
+			max_execution_time=28800
 			if [ "${JUSER}" != "root" ]; then
 				chown -R ${JUSER} ${mnt}/wrkdirs
 			fi
@@ -3013,7 +3013,7 @@ _real_build_port() {
 		checksum|*-depends) JUSER=root ;;
 		stage) [ -n "${PORTTESTING}" ] && markfs prestage ${mnt} ;;
 		install)
-			max_execution_time=3600
+			max_execution_time=28800
 			JUSER=root
 			[ -n "${PORTTESTING}" ] && markfs preinst ${mnt}
 			;;
@@ -3032,7 +3032,7 @@ _real_build_port() {
 			fi
 			;;
 		deinstall)
-			max_execution_time=3600
+			max_execution_time=28800
 			JUSER=root
 			# Skip for all linux ports, they are not safe
 			if [ "${PKGNAME%%*linux*}" != "" ]; then
@@ -4875,7 +4875,7 @@ delete_old_pkg() {
 	_my_path mnt
 
 	if [ ! -d "${mnt}${PORTSDIR}/${origin}" ]; then
-		msg "Deleting ${pkg##*/}: stale package: nonexistent origin ${origin}"
+		msg "${COLOR_DELETE_PKG}Deleting ${pkg##*/}: stale package: nonexistent origin ${origin}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -4910,7 +4910,7 @@ delete_old_pkg() {
 		# with a different origin.  Such as lang/perl5.20 vs
 		# lang/perl5.22 both with 'perl5' as PKGBASE.  A pkgclean
 		# would handle removing this.
-		msg "Deleting ${pkg##*/}: stale package: unwanted origin ${originspec}"
+		msg "${COLOR_DELETE_PKG_NEWDEP}Deleting ${pkg##*/}: stale package: unwanted origin ${originspec}"
 		delete_pkg "${pkg}"
 		return 0
 	fi
@@ -4921,14 +4921,14 @@ delete_old_pkg() {
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
@@ -4936,7 +4936,7 @@ delete_old_pkg() {
 	if have_ports_feature FLAVORS; then
 		shash_get pkgname-flavor "${pkgname}" flavor || flavor=
 		if [ "${pkg_flavor}" != "${flavor}" ]; then
-			msg "Deleting ${pkg##*/}: FLAVOR changed to '${flavor}' from '${pkg_flavor}'"
+			msg "${COLOR_DELETE_PKG_NEW}Deleting ${pkg##*/}: FLAVOR changed to '${flavor}' from '${pkg_flavor}'"
 			delete_pkg "${pkg}"
 			return 0
 		fi
@@ -5053,7 +5053,7 @@ delete_old_pkg() {
 					*) ;;
 					esac
 				fi
-				msg "Deleting ${pkg##*/}: new dependency: ${d}"
+				msg "${COLOR_DELETE_PKG_NEWDEP}Deleting ${pkg##*/}: new dependency: ${d}"
 				delete_pkg "${pkg}"
 				return 0
 				;;
@@ -5083,7 +5083,7 @@ delete_old_pkg() {
 		pkg_get_options compiled_options "${pkg}"
 
 		if [ "${compiled_options}" != "${current_options}" ]; then
-			msg "Deleting ${pkg##*/}: changed options"
+			msg "${COLOR_DELETE_PKG_OPTS}Deleting ${pkg##*/}: changed options"
 			if [ "${CHECK_CHANGED_OPTIONS}" = "verbose" ]; then
 				msg "Pkg: ${compiled_options}"
 				msg "New: ${current_options}"
@@ -6583,7 +6583,7 @@ prepare_ports() {
 			listed_pkgnames | while read pkgname; do
 				pkg="${PACKAGES}/All/${pkgname}.${PKG_EXT}"
 				if [ -f "${pkg}" ]; then
-					msg "(-C) Deleting existing package: ${pkg##*/}"
+					msg "${COLOR_DELETE_PKG}(-C) Deleting existing package: ${pkg##*/}"
 					delete_pkg_xargs "${delete_pkg_list}" \
 					    "${pkg}"
 				fi
@@ -7325,10 +7325,10 @@ DRY_RUN=0
 
 # Be sure to update poudriere.conf to document the default when changing these
 : ${RESOLV_CONF="/etc/resolv.conf"}
-: ${MAX_EXECUTION_TIME:=86400}         # 24 hours for 1 command (phase)
-: ${NOHANG_TIME:=7200}                 # 120 minutes with no log update
-: ${QEMU_MAX_EXECUTION_TIME:=345600}   # 4 days for 1 command (phase)
-: ${QEMU_NOHANG_TIME:=21600}           # 6 hours with no log update
+: ${MAX_EXECUTION_TIME:=172800}         # 48 hours for 1 command (phase)
+: ${NOHANG_TIME:=14400}                 # 240 minutes with no log update
+: ${QEMU_MAX_EXECUTION_TIME:=691200}   # 8 days for 1 command (phase)
+: ${QEMU_NOHANG_TIME:=43200}           # 12 hours with no log update
 : ${TIMESTAMP_LOGS:=no}
 : ${ATOMIC_PACKAGE_REPOSITORY:=yes}
 : ${KEEP_OLD_PACKAGES:=no}
