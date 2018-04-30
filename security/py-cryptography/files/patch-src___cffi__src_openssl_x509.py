--- src/_cffi_src/openssl/x509.py.orig	2017-11-30 01:53:32 UTC
+++ src/_cffi_src/openssl/x509.py
@@ -359,7 +359,7 @@ int X509_get_signature_nid(const X509 *x
 
 /* Added in 1.0.2 but we need it in all versions now due to the great
    opaquing. */
-#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_102
+#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_102 || CRYPTOGRAPHY_IS_LIBRESSL
 /* from x509/x_x509.c */
 int i2d_re_X509_tbs(X509 *x, unsigned char **pp)
 {
@@ -406,10 +406,6 @@ int i2d_re_X509_REQ_tbs(X509_REQ *req, u
     req->req_info->enc.modified = 1;
     return i2d_X509_REQ_INFO(req->req_info, pp);
 }
-int i2d_re_X509_CRL_tbs(X509_CRL *crl, unsigned char **pp) {
-    crl->crl->enc.modified = 1;
-    return i2d_X509_CRL_INFO(crl->crl, pp);
-}
 
 void X509_CRL_get0_signature(const X509_CRL *crl, const ASN1_BIT_STRING **psig,
                              const X509_ALGOR **palg)
@@ -428,4 +424,16 @@ const ASN1_INTEGER *X509_REVOKED_get0_se
     return x->serialNumber;
 }
 #endif
+#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110 || CRYPTOGRAPHY_IS_LIBRESSL
+int i2d_re_X509_CRL_tbs(X509_CRL *crl, unsigned char **pp) {
+    crl->crl->enc.modified = 1;
+    return i2d_X509_CRL_INFO(crl->crl, pp);
+}
+
+int i2d_re_X509_REQ_tbs(X509_REQ *req, unsigned char **pp)
+{
+    req->req_info->enc.modified = 1;
+    return i2d_X509_REQ_INFO(req->req_info, pp);
+}
+#endif
 """
