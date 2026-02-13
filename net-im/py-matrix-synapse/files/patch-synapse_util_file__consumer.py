--- synapse/util/file_consumer.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/util/file_consumer.py
@@ -19,7 +19,7 @@
 #
 
 import queue
-from typing import Any, BinaryIO, cast
+from typing import Any, BinaryIO, Optional, Union, cast
 
 from twisted.internet import threads
 from twisted.internet.defer import Deferred
@@ -50,7 +50,7 @@ class BackgroundFileConsumer:
         self._reactor: ISynapseReactor = reactor
 
         # Producer we're registered with
-        self._producer: IPushProducer | IPullProducer | None = None
+        self._producer: Optional[Union[IPushProducer, IPullProducer]] = None
 
         # True if PushProducer, false if PullProducer
         self.streaming = False
@@ -72,7 +72,7 @@ class BackgroundFileConsumer:
         self._write_exception: Exception | None = None
 
     def registerProducer(
-        self, producer: IPushProducer | IPullProducer, streaming: bool
+        self, producer: Union[IPushProducer, IPullProducer], streaming: bool
     ) -> None:
         """Part of IConsumer interface
 
