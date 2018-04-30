--- src/_cffi_src/openssl/x509_vfy.py.orig	2017-11-30 01:53:32 UTC
+++ src/_cffi_src/openssl/x509_vfy.py
@@ -257,6 +257,20 @@ void (*X509_VERIFY_PARAM_set_hostflags)(
                                         unsigned int) = NULL;
 #endif
 
+#if CRYPTOGRAPHY_OPENSSL_102_OR_GREATER && CRYPTOGRAPHY_IS_LIBRESSL
+static const long X509_V_ERR_SUITE_B_INVALID_VERSION = 0;
+static const long X509_V_ERR_SUITE_B_INVALID_ALGORITHM = 0;
+static const long X509_V_ERR_SUITE_B_INVALID_CURVE = 0;
+static const long X509_V_ERR_SUITE_B_INVALID_SIGNATURE_ALGORITHM = 0;
+static const long X509_V_ERR_SUITE_B_LOS_NOT_ALLOWED = 0;
+static const long X509_V_ERR_SUITE_B_CANNOT_SIGN_P_384_WITH_P_256 = 0;
+/* X509_V_FLAG_TRUSTED_FIRST is also new in 1.0.2+, but it is added separately
+   below because it shows up in some earlier 3rd party OpenSSL packages. */
+static const long X509_V_FLAG_SUITEB_128_LOS_ONLY = 0;
+static const long X509_V_FLAG_SUITEB_192_LOS = 0;
+static const long X509_V_FLAG_SUITEB_128_LOS = 0;
+#endif
+
 /* OpenSSL 1.0.2+ or Solaris's backport */
 #ifdef X509_V_FLAG_PARTIAL_CHAIN
 static const long Cryptography_HAS_X509_V_FLAG_PARTIAL_CHAIN = 1;
@@ -297,7 +311,7 @@ X509 *X509_OBJECT_get0_X509(X509_OBJECT 
 }
 #endif
 
-#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110
+#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110 || CRYPTOGRAPHY_IS_LIBRESSL
 static const long Cryptography_HAS_X509_STORE_CTX_GET_ISSUER = 0;
 typedef void *X509_STORE_CTX_get_issuer_fn;
 X509_STORE_CTX_get_issuer_fn (*X509_STORE_get_get_issuer)(X509_STORE *) = NULL;
