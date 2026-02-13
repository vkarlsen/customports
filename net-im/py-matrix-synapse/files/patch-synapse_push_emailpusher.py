--- synapse/push/emailpusher.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/push/emailpusher.py
@@ -20,7 +20,7 @@
 #
 
 import logging
-from typing import TYPE_CHECKING
+from typing import TYPE_CHECKING, Optional
 
 from twisted.internet.error import AlreadyCalled, AlreadyCancelled
 from twisted.internet.interfaces import IDelayedCall
@@ -71,7 +71,7 @@ class EmailPusher(Pusher):
         self.server_name = hs.hostname
         self.store = self.hs.get_datastores().main
         self.email = pusher_config.pushkey
-        self.timed_call: IDelayedCall | None = None
+        self.timed_call: Optional[IDelayedCall] = None
         self.throttle_params: dict[str, ThrottleParams] = {}
         self._inited = False
 
