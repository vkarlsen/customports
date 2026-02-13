--- synapse/push/httppusher.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/push/httppusher.py
@@ -21,7 +21,7 @@
 import logging
 import random
 import urllib.parse
-from typing import TYPE_CHECKING
+from typing import TYPE_CHECKING, Optional
 
 from prometheus_client import Counter
 
@@ -120,7 +120,7 @@ class HttpPusher(Pusher):
         self.data = pusher_config.data
         self.backoff_delay = HttpPusher.INITIAL_BACKOFF_SEC
         self.failing_since = pusher_config.failing_since
-        self.timed_call: IDelayedCall | None = None
+        self.timed_call: Optional[IDelayedCall] = None
         self._is_processing = False
         self._group_unread_count_by_room = (
             hs.config.push.push_group_unread_count_by_room
