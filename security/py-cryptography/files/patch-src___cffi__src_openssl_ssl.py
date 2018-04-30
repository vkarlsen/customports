--- src/_cffi_src/openssl/ssl.py.orig	2017-11-30 01:53:32 UTC
+++ src/_cffi_src/openssl/ssl.py
@@ -578,7 +578,7 @@ static const long Cryptography_HAS_SSL_C
 
 /* in OpenSSL 1.1.0 the SSL_ST values were renamed to TLS_ST and several were
    removed */
-#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110
+#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110 || CRYPTOGRAPHY_IS_LIBRESSL
 static const long Cryptography_HAS_SSL_ST = 1;
 #else
 static const long Cryptography_HAS_SSL_ST = 0;
@@ -587,7 +587,7 @@ static const long SSL_ST_OK = 0;
 static const long SSL_ST_INIT = 0;
 static const long SSL_ST_RENEGOTIATE = 0;
 #endif
-#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER
+#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER && !CRYPTOGRAPHY_IS_LIBRESSL
 static const long Cryptography_HAS_TLS_ST = 1;
 #else
 static const long Cryptography_HAS_TLS_ST = 0;
