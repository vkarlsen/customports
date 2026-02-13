--- synapse/handlers/user_directory.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/handlers/user_directory.py
@@ -21,7 +21,7 @@
 
 import logging
 from http import HTTPStatus
-from typing import TYPE_CHECKING
+from typing import TYPE_CHECKING, Optional
 
 from twisted.internet.interfaces import IDelayedCall
 
@@ -125,7 +125,7 @@ class UserDirectoryHandler(StateDeltasHandler):
         # Guard to ensure we only have one process for refreshing remote profiles
         self._is_refreshing_remote_profiles = False
         # Handle to cancel the `call_later` of `kick_off_remote_profile_refresh_process`
-        self._refresh_remote_profiles_call_later: IDelayedCall | None = None
+        self._refresh_remote_profiles_call_later: Optional[IDelayedCall] = None
 
         # Guard to ensure we only have one process for refreshing remote profiles
         # for the given servers.
