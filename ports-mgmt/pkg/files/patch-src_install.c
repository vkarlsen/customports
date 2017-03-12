--- src/install.c.orig	2017-03-08 20:19:09 UTC
+++ src/install.c
@@ -232,7 +232,7 @@ exec_install(int argc, char **argv)
 			    nbactions, pkg_jobs_total(jobs));
 
 			if (!dry_run) {
-				rc = query_yesno(false,
+				rc = query_yesno(true,
 				    "\nProceed with this action? ");
 			} else {
 				rc = false;
