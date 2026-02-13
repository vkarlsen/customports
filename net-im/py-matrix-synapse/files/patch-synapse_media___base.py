--- synapse/media/_base.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/media/_base.py
@@ -30,6 +30,7 @@ from typing import (
     Awaitable,
     BinaryIO,
     Generator,
+    Optional,
 )
 
 import attr
@@ -705,7 +706,7 @@ class ThreadedFileSender:
 
         self.file: BinaryIO | None = None
         self.deferred: "Deferred[None]" = Deferred()
-        self.consumer: interfaces.IConsumer | None = None
+        self.consumer: Optional[IConsumer] = None
 
         # Signals if the thread should keep reading/sending data. Set means
         # continue, clear means pause.
