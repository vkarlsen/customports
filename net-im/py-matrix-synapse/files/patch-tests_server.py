--- tests/server.py.orig	1970-01-01 00:00:00 UTC
+++ tests/server.py
@@ -146,7 +146,7 @@ class FakeChannel:
     _reactor: MemoryReactorClock
     result: dict = attr.Factory(dict)
     _ip: str = "127.0.0.1"
-    _producer: IPullProducer | IPushProducer | None = None
+    _producer: Optional[Union[IPullProducer, IPushProducer]] = None
     resource_usage: ContextResourceUsage | None = None
     _request: Request | None = None
 
@@ -248,7 +248,7 @@ class FakeChannel:
         # TODO This should ensure that the IProducer is an IPushProducer or
         # IPullProducer, unfortunately twisted.protocols.basic.FileSender does
         # implement those, but doesn't declare it.
-        self._producer = cast(IPushProducer | IPullProducer, producer)
+        self._producer = cast(Union[IPushProducer, IPullProducer], producer)
         self.producerStreaming = streaming
 
         def _produce() -> None:
@@ -841,7 +841,7 @@ class FakeTransport:
     """Test reactor
     """
 
-    _protocol: IProtocol | None = None
+    _protocol: Optional[IProtocol] = None
     """The Protocol which is producing data for this transport. Optional, but if set
     will get called back for connectionLost() notifications etc.
     """
@@ -860,7 +860,7 @@ class FakeTransport:
     disconnected = False
     connected = True
     buffer: bytes = b""
-    producer: IPushProducer | None = None
+    producer: Optional[IPushProducer] = None
     autoflush: bool = True
 
     def getPeer(self) -> IPv4Address | IPv6Address:
@@ -1062,7 +1062,7 @@ def setup_test_homeserver(
     cleanup_func: Callable[[Callable[[], Optional["Deferred[None]"]]], None],
     server_name: str = "test",
     config: HomeServerConfig | None = None,
-    reactor: ISynapseReactor | None = None,
+    reactor: Optional[ISynapseReactor] = None,
     homeserver_to_use: type[HomeServer] = TestHomeServer,
     db_txn_limit: int | None = None,
     **extra_homeserver_attributes: Any,
