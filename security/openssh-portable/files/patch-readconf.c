--- readconf.c.orig	2019-07-19 17:59:51 UTC
+++ readconf.c
@@ -2017,7 +2017,7 @@ fill_default_options(Options * options)
 	if (options->batch_mode == -1)
 		options->batch_mode = 0;
 	if (options->check_host_ip == -1)
-		options->check_host_ip = 1;
+		options->check_host_ip = 0;
 	if (options->strict_host_key_checking == -1)
 		options->strict_host_key_checking = SSH_STRICT_HOSTKEY_ASK;
 	if (options->compression == -1)
