--- snmplib/snmp_openssl.c.orig	2021-05-25 22:19:35 UTC
+++ snmplib/snmp_openssl.c
@@ -899,6 +899,11 @@ netsnmp_openssl_cert_issued_by(X509 *issuer, X509 *cer
 
 
 #ifndef NETSNMP_FEATURE_REMOVE_OPENSSL_ERR_LOG
+#ifndef ERR_GET_FUNC
+/* removed in OpenSSL 3.0 */
+#define ERR_GET_FUNC(e) -1
+#endif
+
 void
 netsnmp_openssl_err_log(const char *prefix)
 {
