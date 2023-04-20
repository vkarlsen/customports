# Workaround https://bugzilla.gnome.org/show_bug.cgi?id=789714
# Obtained from openSuse / Fedora

--- python/libxml.c.orig	2023-04-11 10:36:35 UTC
+++ python/libxml.c
@@ -1621,6 +1621,7 @@ libxml_xmlErrorFuncHandler(ATTRIBUTE_UNUSED void *ctx,
     PyObject *message;
     PyObject *result;
     char str[1000];
+    unsigned char *ptr = (unsigned char *)str;
 
 #ifdef DEBUG_ERROR
     printf("libxml_xmlErrorFuncHandler(%p, %s, ...) called\n", ctx, msg);
@@ -1637,12 +1638,20 @@ libxml_xmlErrorFuncHandler(ATTRIBUTE_UNUSED void *ctx,
 	    str[999] = 0;
         va_end(ap);
 
+#if PY_MAJOR_VERSION >= 3
+        /* Ensure the error string doesn't start at UTF8 continuation. */
+        while (*ptr && (*ptr & 0xc0) == 0x80)
+            ptr++;
+#endif
+
         list = PyTuple_New(2);
         PyTuple_SetItem(list, 0, libxml_xmlPythonErrorFuncCtxt);
         Py_XINCREF(libxml_xmlPythonErrorFuncCtxt);
-        message = libxml_charPtrConstWrap(str);
+        message = libxml_charPtrConstWrap(ptr);
         PyTuple_SetItem(list, 1, message);
         result = PyEval_CallObject(libxml_xmlPythonErrorFuncHandler, list);
+        /* Forget any errors caused in the error handler. */
+        PyErr_Clear();
         Py_XDECREF(list);
         Py_XDECREF(result);
     }
