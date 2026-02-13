--- synapse/app/generic_worker.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/app/generic_worker.py
@@ -21,6 +21,7 @@
 #
 import logging
 import sys
+from typing import Optional
 
 from twisted.web.resource import Resource
 
@@ -335,7 +336,7 @@ def load_config(argv_options: list[str]) -> HomeServer
 
 def create_homeserver(
     config: HomeServerConfig,
-    reactor: ISynapseReactor | None = None,
+    reactor: Optional[ISynapseReactor] = None,
 ) -> GenericWorkerServer:
     """
     Create a homeserver instance for the Synapse worker process.
