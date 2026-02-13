--- synapse/logging/handlers.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/logging/handlers.py
@@ -3,7 +3,7 @@ import time
 from logging import Handler, LogRecord
 from logging.handlers import MemoryHandler
 from threading import Thread
-from typing import cast
+from typing import Optional, cast
 
 from twisted.internet.interfaces import IReactorCore
 
@@ -26,7 +26,7 @@ class PeriodicallyFlushingMemoryHandler(MemoryHandler)
         target: Handler | None = None,
         flushOnClose: bool = True,
         period: float = 5.0,
-        reactor: IReactorCore | None = None,
+        reactor: Optional[IReactorCore] = None,
     ) -> None:
         """
         period: the period between automatic flushes
