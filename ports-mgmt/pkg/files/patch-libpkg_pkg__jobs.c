--- libpkg/pkg_jobs.c.orig	2020-02-21 14:18:42 UTC
+++ libpkg/pkg_jobs.c
@@ -76,7 +76,7 @@ struct pkg_jobs_locked {
 	int (*locked_pkg_cb)(struct pkg *, void *);
 	void *context;
 };
-static __thread struct pkg_jobs_locked *pkgs_job_lockedpkg;
+static struct pkg_jobs_locked *pkgs_job_lockedpkg;
 
 #define IS_DELETE(j) ((j)->type == PKG_JOBS_DEINSTALL || (j)->type == PKG_JOBS_AUTOREMOVE)
 
