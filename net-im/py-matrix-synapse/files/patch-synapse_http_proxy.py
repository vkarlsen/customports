--- synapse/http/proxy.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/http/proxy.py
@@ -22,7 +22,7 @@
 import json
 import logging
 import urllib.parse
-from typing import TYPE_CHECKING, Any, cast
+from typing import TYPE_CHECKING, Any, Optional, cast
 
 from twisted.internet import protocol
 from twisted.internet.interfaces import ITCPTransport
@@ -237,7 +237,7 @@ class _ProxyResponseBody(protocol.Protocol):
     request.
     """
 
-    transport: ITCPTransport | None = None
+    transport: Optional[ITCPTransport] = None
 
     def __init__(self, request: "SynapseRequest") -> None:
         self._request = request
