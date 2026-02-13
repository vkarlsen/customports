--- synapse/http/federation/matrix_federation_agent.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/http/federation/matrix_federation_agent.py
@@ -19,7 +19,7 @@
 #
 import logging
 import urllib.parse
-from typing import Any, Generator
+from typing import Any, Generator, Optional
 from urllib.request import (  # type: ignore[attr-defined]
     proxy_bypass_environment,
 )
@@ -173,7 +173,7 @@ class MatrixFederationAgent:
         method: bytes,
         uri: bytes,
         headers: Headers | None = None,
-        bodyProducer: IBodyProducer | None = None,
+        bodyProducer: Optional[IBodyProducer] = None,
     ) -> Generator[defer.Deferred, Any, IResponse]:
         """
         Args:
