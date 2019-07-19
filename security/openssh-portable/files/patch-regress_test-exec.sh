--- regress/test-exec.sh.orig	2019-04-17 22:52:57 UTC
+++ regress/test-exec.sh
@@ -419,6 +419,7 @@ cat << EOF > $OBJ/sshd_config
 	LogLevel		DEBUG3
 	AcceptEnv		_XXX_TEST_*
 	AcceptEnv		_XXX_TEST
+	PermitRootLogin		yes
 	Subsystem	sftp	$SFTPSERVER
 EOF
 
