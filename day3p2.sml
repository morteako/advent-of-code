fun readlist (infile : string) = let
  val ins = TextIO.openIn infile
  fun loop ins =
   case TextIO.inputLine ins of
      SOME line => line :: loop ins
    | NONE      => []
in
  loop ins before TextIO.closeIn ins
end;

exception Excp;

val lines = readlist("day3.txt");

fun f #" " = true
|   f #"\n" = true
|   f _  = false;

fun toInt str = case Int.fromString str of SOME(x) => x | NONE => raise Excp;   

val cleanLines = map (String.tokens f) lines;
val intLines = map (map toInt) cleanLines;

fun validTriangle nrs = 
    let
        val [a,b,c] = ListMergeSort.sort op> nrs
    in
        if a+b > c then 1 else 0
    end;

(* Part1         *)
foldr (fn (x,y) => validTriangle x + y) 0 intLines;

(* Part2 *)

fun conv ([a,b,c]::[d,e,f]::[g,i,h]::rest) = conv rest @ [[a,d,g],[b,e,i],[c,f,h]]
|   conv _ = [];

foldr (fn (x,y) => validTriangle x + y) 0 (conv intLines);