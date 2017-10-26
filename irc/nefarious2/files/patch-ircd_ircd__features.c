--- ircd/ircd_features.c.orig	2017-09-23 19:36:50 UTC
+++ ircd/ircd_features.c
@@ -559,7 +559,7 @@ static struct FeatureDesc {
   /* Some misc. default paths */
   F_S(MPATH, FEAT_CASE | FEAT_MYOPER, "ircd.motd", motd_init),
   F_S(RPATH, FEAT_CASE | FEAT_MYOPER, "remote.motd", motd_init),
-  F_S(PPATH, FEAT_CASE | FEAT_MYOPER | FEAT_READ, "ircd.pid", 0),
+  F_S(PPATH, FEAT_CASE | FEAT_MYOPER | FEAT_READ, "/var/run/nefarious2/ircd.pid", 0),
 
   /* Networking features */
   F_I(TOS_SERVER, 0, 0x08, 0),
