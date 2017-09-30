--- lang_js/analyze/module_js.ml.orig	2015-03-03 18:52:16 UTC
+++ lang_js/analyze/module_js.ml
@@ -48,50 +48,50 @@ type shape =
 	| LiteralShape
 	| ArrayShape
 
-	(** _((id,container,maps) ref) **)
+	(* _((id,container,maps) ref) *)
 	(* this is a ref to allow extensible representations *)
 	(* id is unique, and is used to prune infinite recursion *)
 	(* maps is an ObjectShape list *)
 	| ObjectShape of (int * shape smap * shape list) ref
 
-	(** _(block,constructor) **)
+	(* _(block,constructor) *)
 	(* block is an ObjectShape *)
 	(* constructor is a ClassShape *)
     | FunctionShape of shape Common.smap ref * shape
 
-	(** _(module) **)
+	(* _(module) *)
 	| RequireShape of module_
 
-	(** _(reason) **)
+	(* _(reason) *)
 	| UnknownShape of string
 
-	(** _(instance, static) **)
+	(* _(instance, static) *)
 	(* instance is a ObjectShape *)
 	(* static is a ObjectShape where static.prototype is a ObjectShape *)
 	| ClassShape of shape * shape
 
-	(** _(class) **)
+	(* _(class) *)
 	(* class is a ClassShape *)
 	(* returns an ObjectShape *)
 	| NewShape of shape
 
-	(** _(maps) **)
+	(* _(maps) *)
 	(* maps is an ObjectShape *)
 	(* returns a ClassShape *)
 	| MixinShape of shape
 
-	(** _(class,mixin) **)
+	(* _(class,mixin) *)
 	(* class is a ClassShape, mixin is a ClassShape *)
 	(* returns a ClassShape *)
 	| ClassWithMixinShape of shape * shape
 
-	(** _(object,prop) **)
+	(* _(object,prop) *)
 	| PropertyShape of shape * string
 
-	(** _(function) **)
+	(* _(function) *)
 	| ApplyShape of shape
 
-	(** _(array) **)
+	(* _(array) *)
 	| ElementShape of shape
 
 let fresh_id =
