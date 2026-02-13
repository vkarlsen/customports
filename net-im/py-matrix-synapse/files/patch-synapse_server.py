--- synapse/server.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/server.py
@@ -34,6 +34,7 @@ from typing import (
     Any,
     Awaitable,
     Callable,
+    Optional,
     TypeVar,
     cast,
 )
@@ -319,7 +320,7 @@ class HomeServer(metaclass=abc.ABCMeta):
         self,
         hostname: str,
         config: HomeServerConfig,
-        reactor: ISynapseReactor | None = None,
+        reactor: Optional[ISynapseReactor] = None,
     ):
         """
         Args:
@@ -352,7 +353,7 @@ class HomeServer(metaclass=abc.ABCMeta):
         self._module_web_resources_consumed = False
 
         # This attribute is set by the free function `refresh_certificate`.
-        self.tls_server_context_factory: IOpenSSLContextFactory | None = None
+        self.tls_server_context_factory: Optional[IOpenSSLContextFactory] = None
 
         self._is_shutdown = False
         self._async_shutdown_handlers: list[ShutdownInfo] = []
