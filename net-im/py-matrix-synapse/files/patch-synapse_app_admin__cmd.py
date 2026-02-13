--- synapse/app/admin_cmd.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/app/admin_cmd.py
@@ -24,7 +24,7 @@ import logging
 import os
 import sys
 import tempfile
-from typing import Mapping, Sequence
+from typing import Mapping, Optional, Sequence
 
 from twisted.internet import defer, task
 
@@ -291,7 +291,7 @@ def load_config(argv_options: list[str]) -> tuple[Home
 
 def create_homeserver(
     config: HomeServerConfig,
-    reactor: ISynapseReactor | None = None,
+    reactor: Optional[ISynapseReactor] = None,
 ) -> AdminCmdServer:
     """
     Create a homeserver instance for the Synapse admin command process.
