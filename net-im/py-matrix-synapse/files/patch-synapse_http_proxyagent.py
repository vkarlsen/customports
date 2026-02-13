--- synapse/http/proxyagent.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/http/proxyagent.py
@@ -21,7 +21,7 @@
 import logging
 import random
 import re
-from typing import Any, Collection, Sequence, cast
+from typing import Any, Collection, Optional, Sequence, cast
 from urllib.parse import urlparse
 from urllib.request import (  # type: ignore[attr-defined]
     proxy_bypass_environment,
@@ -119,8 +119,8 @@ class ProxyAgent(_AgentBase):
         self,
         *,
         reactor: IReactorCore,
-        proxy_reactor: IReactorCore | None = None,
-        contextFactory: IPolicyForHTTPS | None = None,
+        proxy_reactor: Optional[IReactorCore] = None,
+        contextFactory: Optional[IPolicyForHTTPS] = None,
         connectTimeout: float | None = None,
         bindAddress: bytes | None = None,
         pool: HTTPConnectionPool | None = None,
@@ -175,7 +175,7 @@ class ProxyAgent(_AgentBase):
         self._policy_for_https = contextFactory
         self._reactor = cast(IReactorTime, reactor)
 
-        self._federation_proxy_endpoint: IStreamClientEndpoint | None = None
+        self._federation_proxy_endpoint: Optional[IStreamClientEndpoint] = None
         self._federation_proxy_credentials: ProxyCredentials | None = None
         if federation_proxy_locations:
             assert federation_proxy_credentials is not None, (
@@ -221,7 +221,7 @@ class ProxyAgent(_AgentBase):
         method: bytes,
         uri: bytes,
         headers: Headers | None = None,
-        bodyProducer: IBodyProducer | None = None,
+        bodyProducer: Optional[IBodyProducer] = None,
     ) -> "defer.Deferred[IResponse]":
         """
         Issue a request to the server indicated by the given uri.
@@ -365,11 +365,11 @@ class ProxyAgent(_AgentBase):
 def http_proxy_endpoint(
     proxy: bytes | None,
     reactor: IReactorCore,
-    tls_options_factory: IPolicyForHTTPS | None,
+    tls_options_factory: Optional[IPolicyForHTTPS],
     timeout: float = 30,
     bindAddress: bytes | str | tuple[bytes | str, int] | None = None,
     attemptDelay: float | None = None,
-) -> tuple[IStreamClientEndpoint | None, ProxyCredentials | None]:
+) -> tuple[Optional[IStreamClientEndpoint], ProxyCredentials | None]:
     """Parses an http proxy setting and returns an endpoint for the proxy
 
     Args:
