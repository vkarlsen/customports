--- synapse/handlers/message.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/handlers/message.py
@@ -22,7 +22,7 @@
 import logging
 import random
 from http import HTTPStatus
-from typing import TYPE_CHECKING, Any, Mapping, Sequence
+from typing import TYPE_CHECKING, Any, Mapping, Optional, Sequence
 
 from canonicaljson import encode_canonical_json
 
@@ -111,7 +111,7 @@ class MessageHandler:
 
         # The scheduled call to self._expire_event. None if no call is currently
         # scheduled.
-        self._scheduled_expiry: IDelayedCall | None = None
+        self._scheduled_expiry: Optional[IDelayedCall] = None
 
         if not hs.config.worker.worker_app:
             self.hs.run_as_background_process(
