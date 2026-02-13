--- synapse/app/_base.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/app/_base.py
@@ -36,6 +36,7 @@ from typing import (
     Awaitable,
     Callable,
     NoReturn,
+    Optional,
     cast,
 )
 from wsgiref.simple_server import WSGIServer
@@ -419,7 +420,7 @@ def listen_http(
     root_resource: Resource,
     version_string: str,
     max_request_body_size: int,
-    context_factory: IOpenSSLContextFactory | None,
+    context_factory: Optional[IOpenSSLContextFactory],
     reactor: ISynapseReactor = reactor,
 ) -> list[Port]:
     """
