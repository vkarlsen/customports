--- libpkg/pkg_add.c.orig	2017-11-15 09:56:10 UTC
+++ libpkg/pkg_add.c
@@ -953,14 +953,21 @@ pkg_add_cleanup_old(struct pkgdb *db, st
 	 * Execute pre deinstall scripts
 	 */
 	if ((flags & PKG_ADD_NOSCRIPT) == 0) {
-		if ((flags & PKG_ADD_USE_UPGRADE_SCRIPTS) == PKG_ADD_USE_UPGRADE_SCRIPTS)
-			ret = pkg_script_run(old, PKG_SCRIPT_PRE_UPGRADE);
-		else
-			ret = pkg_script_run(old, PKG_SCRIPT_PRE_DEINSTALL);
-		if (ret != EPKG_OK && pkg_object_bool(pkg_config_get("DEVELOPER_MODE")))
-			return (ret);
-		else
-			ret = EPKG_OK;
+		bool buggydeinstall = false;
+		if (strcmp(old->name, "javavmwrapper") == 0 &&
+		    (strcmp(old->version, "2.5") == 0 ||
+		    strcmp(old->version, "2.5_1") == 0))
+			buggydeinstall = true;
+		if (!buggydeinstall) {
+			if ((flags & PKG_ADD_USE_UPGRADE_SCRIPTS) == PKG_ADD_USE_UPGRADE_SCRIPTS)
+				ret = pkg_script_run(old, PKG_SCRIPT_PRE_UPGRADE);
+			else
+				ret = pkg_script_run(old, PKG_SCRIPT_PRE_DEINSTALL);
+			if (ret != EPKG_OK && pkg_object_bool(pkg_config_get("DEVELOPER_MODE")))
+				return (ret);
+			else
+				ret = EPKG_OK;
+		}
 	}
 
 	/* Now remove files that no longer exist in the new package */
