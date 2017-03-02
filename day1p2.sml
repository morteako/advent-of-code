exception Excp;


fun split str = 
    case Int.fromString(String.substring(str, 1, String.size(str) - 1)) of
        NONE => raise Excp
    |   SOME(x) => (String.sub(str,0),x);

datatype point = Point of int * int;

fun nextDirIndex #"R" i =(i + 1) mod 4
|   nextDirIndex #"L" i =(i - 1) mod 4
|   nextDirIndex _ _ = raise Excp;


fun getDir i = List.nth([(0,1), (1,0), (0,~1), (~1,0)], i);


fun walk [] _ (Point(x,y)) = [(x,y)]
|   walk (s::ss) dirIndex (Point(x,y)) =
    let
        val (direction, nr) = split s
        val nextDirI = nextDirIndex direction dirIndex
        val (dirX,dirY) = getDir nextDirI
        val range = List.tabulate(nr, fn x => x)
        val steps = map (fn n => (x + dirX*n, y + dirY*n)) range
    in
        steps @ walk ss nextDirI (Point(x + dirX * nr,y + dirY * nr))
    end;
    
(* read line from file *)
val infile = (TextIO.openIn "day1.txt");
val ordersStr = case (TextIO.inputLine infile) of SOME(x) => [x] | NONE => raise Excp;
TextIO.closeIn infile;

(* split on , and remove whitespace *)
fun curry2 f x y = f(x,y);
val ordersSplit =  String.fields (fn c => c = #"," orelse c = #" ") (hd ordersStr);
val ordersFiltered = List.filter ((curry2 op<>) "") ordersSplit;

val tuples = walk ordersFiltered 0 (Point(0,0)); (* get all blocks/points visited *)


val (x,y) = List.last tuples;
val resultPart1 = abs(x)+abs(y);


fun contains _ [] = false
|   contains (x:int*int) (y::ys) = if x = y then true else contains x ys;

fun findFirstDupl [] = raise Excp
|   findFirstDupl (x::xs) = if contains x xs then x else findFirstDupl xs;



val (x,y) = findFirstDupl tuples;
val resultPart2 = abs(x)+abs(y);
