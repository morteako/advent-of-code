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


val splitted = map (String.tokens delim) lines;
val exploded = map (map String.explode) splitted;

fun boolToInt true = 1
|   boolToInt false = 0;

fun hasABBA ((a::b::c::d::rest):char list) = 
        if a <> b andalso a = d andalso b = c then true else (hasABBA (b::c::d::rest))
|   hasABBA _ = false;

exception Invalid;


fun iterate flag [xs] = hasABBA xs orelse flag
|   iterate true (xs::ys::rest) = if hasABBA ys then raise Invalid else iterate true rest
|   iterate false (xs::ys::rest) = if hasABBA ys then raise Invalid else iterate (hasABBA xs) rest
|   iterate flag _ = false;

fun doIterate xs = (iterate false xs) handle Invalid => false;

val ints = map boolToInt (map doIterate exploded);
val part1result = foldr op+ 0 ints;


(* Part 2 *)

fun everyOther [] = []
|   everyOther [x] = [x]
|   everyOther (x::y::rest) = (x::everyOther rest);

fun form xs = (everyOther xs, map String.implode (everyOther (tl xs)));

val formed = map form exploded;


fun inHyper str hyper = foldr (fn (x,y) => if (String.isSubstring str x) then true else y) false hyper;
fun iter ((a::b::c::rest):char list) hyper = 
        if a = c andalso a <> b then 
        inHyper (String.implode([b,a,b])) hyper orelse iter (b::c::rest) hyper 
        else iter (b::c::rest) hyper
|   iter _ hyper = false;    

fun all xs = foldr (fn (x,y) => x andalso y) true xs;
fun any xs = foldr (fn (x,y) => x orelse y) false xs;

fun f(xs,y) = map (fn x => iter x y) xs;

any (f(hd formed));

val fmapped = (map f formed);
val anymapped = (map any fmapped);
val ints = map boolToInt anymapped;
val part1result = part1result;
val part2result = foldr op+ 0 ints;
