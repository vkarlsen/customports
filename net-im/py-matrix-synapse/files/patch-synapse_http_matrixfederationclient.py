--- synapse/http/matrixfederationclient.py.orig	1970-01-01 00:00:00 UTC
+++ synapse/http/matrixfederationclient.py
@@ -33,6 +33,7 @@ from typing import (
     Callable,
     Generic,
     Literal,
+    Optional,
     TextIO,
     TypeVar,
     cast,
@@ -691,7 +692,7 @@ class MatrixFederationHttpClient:
                             destination_bytes, method_bytes, url_to_sign_bytes, json
                         )
                         data = encode_canonical_json(json)
-                        producer: IBodyProducer | None = QuieterFileBodyProducer(
+                        producer: Optional[IBodyProducer] = QuieterFileBodyProducer(
                             BytesIO(data), cooperator=self._cooperator
                         )
                     else:
