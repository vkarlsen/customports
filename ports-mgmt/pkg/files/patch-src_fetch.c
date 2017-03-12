--- src/fetch.c.orig	2017-03-08 20:20:24 UTC
+++ src/fetch.c
@@ -205,11 +205,11 @@ exec_fetch(int argc, char **argv)
 		    "The following packages will be fetched:\n\n");
 
 		if (rc != 0) {
-			rc = query_yesno(false, "\nProceed with fetching "
+			rc = query_yesno(true, "\nProceed with fetching "
 					"packages? ");
 		} else {
 			printf("No packages are required to be fetched.\n");
-			rc = query_yesno(false, "Check the integrity of packages "
+			rc = query_yesno(true, "Check the integrity of packages "
 							"downloaded? ");
 			csum_only = true;
 		}
