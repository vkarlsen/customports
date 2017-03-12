--- src/check.c.orig	2017-03-08 20:19:45 UTC
+++ src/check.c
@@ -203,7 +203,7 @@ fix_deps(struct pkgdb *db, struct deps_e
 	print_jobs_summary(jobs,
 			"The following packages will be installed:\n\n");
 
-	rc = query_yesno(false, "\n>>> Try to fix the missing dependencies? ");
+	rc = query_yesno(true, "\n>>> Try to fix the missing dependencies? ");
 
 	if (rc) {
 		if (pkgdb_access(PKGDB_MODE_WRITE, PKGDB_DB_LOCAL) ==
