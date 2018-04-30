--- src/_cffi_src/openssl/ct.py.orig	2017-11-30 01:53:32 UTC
+++ src/_cffi_src/openssl/ct.py
@@ -5,7 +5,7 @@
 from __future__ import absolute_import, division, print_function
 
 INCLUDES = """
-#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER
+#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER && !CRYPTOGRAPHY_IS_LIBRESSL
 #include <openssl/ct.h>
 
 typedef STACK_OF(SCT) Cryptography_STACK_OF_SCT;
@@ -55,7 +55,7 @@ void SCT_LIST_free(Cryptography_STACK_OF
 """
 
 CUSTOMIZATIONS = """
-#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER
+#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER && !CRYPTOGRAPHY_IS_LIBRESSL
 static const long Cryptography_HAS_SCT = 1;
 #else
 static const long Cryptography_HAS_SCT = 0;
