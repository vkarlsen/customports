--- synapse/http/client.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/http/client.py
@@ -28,6 +28,7 @@ from typing import (
     BinaryIO,
     Callable,
     Mapping,
+    Optional,
     Protocol,
 )
 
@@ -313,7 +314,7 @@ class BlocklistingAgentWrapper(Agent):
         method: bytes,
         uri: bytes,
         headers: Headers | None = None,
-        bodyProducer: IBodyProducer | None = None,
+        bodyProducer: Optional[IBodyProducer] = None,
     ) -> defer.Deferred:
         h = urllib.parse.urlparse(uri.decode("ascii"))
 
@@ -1033,7 +1034,7 @@ class BodyExceededMaxSize(Exception):
 class _DiscardBodyWithMaxSizeProtocol(protocol.Protocol):
     """A protocol which immediately errors upon receiving data."""
 
-    transport: ITCPTransport | None = None
+    transport: Optional[ITCPTransport] = None
 
     def __init__(self, deferred: defer.Deferred):
         self.deferred = deferred
@@ -1075,7 +1076,7 @@ class _MultipartParserProtocol(protocol.Protocol):
     Protocol to read and parse a MSC3916 multipart/mixed response
     """
 
-    transport: ITCPTransport | None = None
+    transport: Optional[ITCPTransport] = None
 
     def __init__(
         self,
@@ -1188,7 +1189,7 @@ class _MultipartParserProtocol(protocol.Protocol):
 class _ReadBodyWithMaxSizeProtocol(protocol.Protocol):
     """A protocol which reads body to a stream, erroring if the body exceeds a maximum size."""
 
-    transport: ITCPTransport | None = None
+    transport: Optional[ITCPTransport] = None
 
     def __init__(
         self, stream: ByteWriteable, deferred: defer.Deferred, max_size: int | None
