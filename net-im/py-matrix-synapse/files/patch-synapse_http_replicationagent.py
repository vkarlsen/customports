--- synapse/http/replicationagent.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/http/replicationagent.py
@@ -20,6 +20,7 @@
 #
 
 import logging
+from typing import Optional
 
 from zope.interface import implementer
 
@@ -149,7 +150,7 @@ class ReplicationAgent(_AgentBase):
         method: bytes,
         uri: bytes,
         headers: Headers | None = None,
-        bodyProducer: IBodyProducer | None = None,
+        bodyProducer: Optional[IBodyProducer] = None,
     ) -> "defer.Deferred[IResponse]":
         """
         Issue a request to the server indicated by the given uri.
