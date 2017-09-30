--- lang_js/analyze/utils_js.mli.orig	2015-03-03 18:52:16 UTC
+++ lang_js/analyze/utils_js.mli
@@ -1,8 +1,8 @@
 
-(** print utils **)
+(* print utils *)
 val string_of_any : Ast_js.any -> string
 
-(** Example: load file task **)
-(** if file exists, unmarshal data in the file and return it **)
-(** otherwise, run task to generate data, store it in the file, and return it **)
+(* Example: load file task *)
+(* if file exists, unmarshal data in the file and return it *)
+(* otherwise, run task to generate data, store it in the file, and return it *)
 val load : Common.filename -> (unit -> 'a) -> 'a
