--- libtiff/tif_print.c.orig	2016-11-25 17:26:23 UTC
+++ libtiff/tif_print.c
@@ -667,13 +667,13 @@ TIFFPrintDirectory(TIFF* tif, FILE* fd, 
 #if defined(__WIN32__) && (defined(_MSC_VER) || defined(__MINGW32__))
 			fprintf(fd, "    %3lu: [%8I64u, %8I64u]\n",
 			    (unsigned long) s,
-			    (unsigned __int64) td->td_stripoffset[s],
-			    (unsigned __int64) td->td_stripbytecount[s]);
+                td->td_stripoffset ? (unsigned __int64) td->td_stripoffset[s] : 0,
+                td->td_stripbytecount ? (unsigned __int64) td->td_stripbytecount[s] : 0);
 #else
 			fprintf(fd, "    %3lu: [%8llu, %8llu]\n",
 			    (unsigned long) s,
-			    (unsigned long long) td->td_stripoffset[s],
-			    (unsigned long long) td->td_stripbytecount[s]);
+                td->td_stripoffset ? (unsigned long long) td->td_stripoffset[s] : 0,
+                td->td_stripbytecount ? (unsigned long long) td->td_stripbytecount[s] : 0);
 #endif
 	}
 }
