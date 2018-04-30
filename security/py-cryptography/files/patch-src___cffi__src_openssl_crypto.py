--- src/_cffi_src/openssl/crypto.py.orig	2017-11-30 01:53:32 UTC
+++ src/_cffi_src/openssl/crypto.py
@@ -92,7 +92,7 @@ CUSTOMIZATIONS = """
 # define OPENSSL_PLATFORM        SSLEAY_PLATFORM
 # define OPENSSL_DIR             SSLEAY_DIR
 #endif
-#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110
+#if CRYPTOGRAPHY_OPENSSL_LESS_THAN_110 || CRYPTOGRAPHY_IS_LIBRESSL
 static const long Cryptography_HAS_LOCKING_CALLBACKS = 1;
 #else
 static const long Cryptography_HAS_LOCKING_CALLBACKS = 0;
