--- synapse/logging/_remote.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/logging/_remote.py
@@ -25,7 +25,7 @@ import traceback
 from collections import deque
 from ipaddress import IPv4Address, IPv6Address, ip_address
 from math import floor
-from typing import Callable
+from typing import Callable, Optional
 
 import attr
 from zope.interface import implementer
@@ -113,7 +113,7 @@ class RemoteHandler(logging.Handler):
         port: int,
         maximum_buffer: int = 1000,
         level: int = logging.NOTSET,
-        _reactor: IReactorTime | None = None,
+        _reactor: Optional[IReactorTime] = None,
     ):
         super().__init__(level=level)
         self.host = host
