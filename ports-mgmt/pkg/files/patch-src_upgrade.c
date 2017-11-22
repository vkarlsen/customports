--- src/upgrade.c.orig	2017-11-22 19:02:54 UTC
+++ src/upgrade.c
@@ -411,7 +411,7 @@ exec_upgrade(int argc, char **argv)
 				nbactions, pkg_jobs_total(jobs));
 
 			if (!dry_run) {
-				rc = query_yesno(false, "\nProceed with this "
+				rc = query_yesno(true, "\nProceed with this "
 						"action? ");
 			} else {
 				rc = false;
