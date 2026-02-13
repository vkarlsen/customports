--- synapse/handlers/delayed_events.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/handlers/delayed_events.py
@@ -13,7 +13,7 @@
 #
 
 import logging
-from typing import TYPE_CHECKING
+from typing import TYPE_CHECKING, Optional
 
 from twisted.internet.interfaces import IDelayedCall
 
@@ -74,7 +74,7 @@ class DelayedEventsHandler:
             cfg=self._config.ratelimiting.rc_delayed_event_mgmt,
         )
 
-        self._next_delayed_event_call: IDelayedCall | None = None
+        self._next_delayed_event_call: Optional[IDelayedCall] = None
 
         # The current position in the current_state_delta stream
         self._event_pos: int | None = None
