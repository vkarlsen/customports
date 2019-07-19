--- servconf.c.orig	2019-07-19 20:11:34 UTC
+++ servconf.c
@@ -41,6 +41,7 @@
 #include <util.h>
 #endif
 
+#include "version.h"
 #include "openbsd-compat/sys-queue.h"
 #include "xmalloc.h"
 #include "ssh.h"
@@ -180,6 +181,7 @@ initialize_server_options(ServerOptions *options)
 	options->fingerprint_hash = -1;
 	options->disable_forwarding = -1;
 	options->expose_userauth_info = -1;
+    options->use_blacklist = -1;
 }
 
 /* Returns 1 if a string option is unset or set to "none" or 0 otherwise. */
@@ -276,7 +278,11 @@ fill_default_server_options(ServerOptions *options)
 
 	/* Portable-specific options */
 	if (options->use_pam == -1)
+#ifdef USE_PAM
+		options->use_pam = 1;
+#else
 		options->use_pam = 0;
+#endif
 
 	/* Standard Options */
 	if (options->num_host_key_files == 0) {
@@ -316,7 +322,7 @@ fill_default_server_options(ServerOptions *options)
 	if (options->print_lastlog == -1)
 		options->print_lastlog = 1;
 	if (options->x11_forwarding == -1)
-		options->x11_forwarding = 0;
+		options->x11_forwarding = 1;
 	if (options->x11_display_offset == -1)
 		options->x11_display_offset = 10;
 	if (options->x11_use_localhost == -1)
@@ -356,7 +362,11 @@ fill_default_server_options(ServerOptions *options)
 	if (options->gss_strict_acceptor == -1)
 		options->gss_strict_acceptor = 1;
 	if (options->password_authentication == -1)
+#ifdef USE_PAM
+		options->password_authentication = 0;
+#else
 		options->password_authentication = 1;
+#endif
 	if (options->kbd_interactive_authentication == -1)
 		options->kbd_interactive_authentication = 0;
 	if (options->challenge_response_authentication == -1)
@@ -425,6 +435,8 @@ fill_default_server_options(ServerOptions *options)
 		options->disable_forwarding = 0;
 	if (options->expose_userauth_info == -1)
 		options->expose_userauth_info = 0;
+    if (options->use_blacklist == -1)
+        options->use_blacklist = 0;
 
 	assemble_algorithms(options);
 
@@ -510,6 +522,7 @@ typedef enum {
 	sStreamLocalBindMask, sStreamLocalBindUnlink,
 	sAllowStreamLocalForwarding, sFingerprintHash, sDisableForwarding,
 	sExposeAuthInfo, sRDomain,
+    sUseBlacklist,
 	sDeprecated, sIgnore, sUnsupported
 } ServerOpCodes;
 
@@ -621,6 +634,7 @@ static struct {
 	{ "maxsessions", sMaxSessions, SSHCFG_ALL },
 	{ "banner", sBanner, SSHCFG_ALL },
 	{ "usedns", sUseDNS, SSHCFG_GLOBAL },
+    { "useblacklist", sUseBlacklist, SSHCFG_GLOBAL },
 	{ "verifyreversemapping", sDeprecated, SSHCFG_GLOBAL },
 	{ "reversemappingcheck", sDeprecated, SSHCFG_GLOBAL },
 	{ "clientaliveinterval", sClientAliveInterval, SSHCFG_ALL },
@@ -2157,6 +2171,10 @@ process_server_config_line(ServerOptions *options, cha
 		intptr = &options->expose_userauth_info;
 		goto parse_flag;
 
+    case sUseBlacklist:
+        intptr = &options->use_blacklist;
+        goto parse_flag;
+
 	case sRDomain:
 		charptr = &options->routing_domain;
 		arg = strdelim(&cp);
@@ -2610,6 +2628,7 @@ dump_config(ServerOptions *o)
 	dump_cfg_fmtint(sStreamLocalBindUnlink, o->fwd_opts.streamlocal_bind_unlink);
 	dump_cfg_fmtint(sFingerprintHash, o->fingerprint_hash);
 	dump_cfg_fmtint(sExposeAuthInfo, o->expose_userauth_info);
+    dump_cfg_fmtint(sUseBlacklist, o->use_blacklist);
 
 	/* string arguments */
 	dump_cfg_string(sPidFile, o->pid_file);
