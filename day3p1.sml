fun readlist (infile : string) = let
  val ins = TextIO.openIn infile
  fun loop ins =
   case TextIO.inputLine ins of
      SOME line => (String.substring(line, 0, String.size(line)-1))  :: loop ins
    | NONE      => []
in
  loop ins before TextIO.closeIn ins
end;

exception Excp;

val lines = readlist("day7.txt");

foldr (fn (x,y)  => if #"[" = String.sub(x,0) then raise Excp else y) true lines;

fun delim #"[" = true
|   delim #"]" = true
|   delim _ = false;


(* val splitted = foldr (fn (x,y) => (String.tokens delim x)::y) [] lines; *)
val splitted = map (String.tokens delim) lines;
val exploded = map (map String.explode) splitted;

fun boolToInt true = 1
|   boolToInt false = 0;

fun hasABBA (a::b::c::d::rest) = if a <> b andalso a = d andalso b = c then true else (hasABBA (b::c::d::rest))
|   hasABBA _ = false;

exception Invalid;

fun iterate flag [xs] = hasABBA xs orelse flag
|   iterate true (xs::ys::rest) = if hasABBA ys then raise Invalid else iterate true rest
|   iterate false (xs::ys::rest) = if hasABBA ys then raise Invalid else iterate (hasABBA xs) rest
|   iterate flag _ = false;
(* foldr (fn (x,y) => validTriangle x + y) 0 intLines; *)

fun doIterate xs = (iterate false xs) handle Invalid => false;

val ints = map boolToInt (map doIterate exploded);
val count = foldr op+ 0 ints;
(* doIterate (hd splitted); *)
(* fun member v xs = foldr (fn (x,y) => x = v orelse y) false xs; *)

(* member 1 [1,2,3,4]; *)
(* member #"i" (String.explode "hei"); *)