--- lib/url.c.orig	2018-10-30 06:47:16 UTC
+++ lib/url.c
@@ -602,6 +602,10 @@ CURLcode Curl_open(struct Curl_easy **cu
 
       data->progress.flags |= PGRS_HIDE;
       data->state.current_speed = -1; /* init to negative == impossible */
+#if defined(__FreeBSD_version)
+      /* different handling of signals and threads */
+      data->set.no_signal = TRUE;
+#endif /* __FreeBSD_version */
 
       Curl_http2_init_state(&data->state);
     }
