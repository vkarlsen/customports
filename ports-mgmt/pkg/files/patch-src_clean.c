--- src/clean.c.orig	2017-10-06 12:00:58 UTC
+++ src/clean.c
@@ -415,7 +415,7 @@ exec_clean(int argc, char **argv)
 	if (!quiet)
 		printf("The cleanup will free %s\n", size);
 	if (!dry_run) {
-			if (query_yesno(false,
+			if (query_yesno(true,
 			  "\nProceed with cleaning the cache? ")) {
 				retcode = delete_dellist(cachefd, cachedir, &dl, kv_size(dl));
 			}
