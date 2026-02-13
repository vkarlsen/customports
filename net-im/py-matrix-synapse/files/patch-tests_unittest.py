--- tests/unittest.py.orig	1970-01-01 00:00:00 UTC
+++ tests/unittest.py
@@ -37,6 +37,7 @@ from typing import (
     Iterable,
     Mapping,
     NoReturn,
+    Optional,
     Protocol,
     TypeVar,
 )
@@ -636,7 +637,7 @@ class HomeserverTestCase(TestCase):
         self,
         server_name: str | None = None,
         config: JsonDict | None = None,
-        reactor: ISynapseReactor | None = None,
+        reactor: Optional[ISynapseReactor] = None,
         clock: Clock | None = None,
         **extra_homeserver_attributes: Any,
     ) -> HomeServer:
