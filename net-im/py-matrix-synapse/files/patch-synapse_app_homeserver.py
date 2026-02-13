--- synapse/app/homeserver.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/app/homeserver.py
@@ -22,7 +22,7 @@
 import logging
 import os
 import sys
-from typing import Iterable
+from typing import Iterable, Optional
 
 from twisted.internet.tcp import Port
 from twisted.web.resource import EncodingResourceWrapper, Resource
@@ -350,7 +350,7 @@ def load_or_generate_config(argv_options: list[str]) -
 
 def create_homeserver(
     config: HomeServerConfig,
-    reactor: ISynapseReactor | None = None,
+    reactor: Optional[ISynapseReactor] = None,
 ) -> SynapseHomeServer:
     """
     Create a homeserver instance for the Synapse main process.
