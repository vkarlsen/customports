--- src/string.hh.orig	2017-02-19 22:16:50 UTC
+++ src/string.hh
@@ -93,7 +93,6 @@ private:
     const Type& type() const { return *static_cast<const Type*>(this); }
 };
 
-[[gnu::optimize(3)]] // this is recursive for constexpr reason
 constexpr ByteCount strlen(const char* s)
 {
     return *s == 0 ? 0 : strlen(s+1) + 1;
