fun f liste = (hd liste);

fun fib 1 = 1
|   fib n = n * fib (n - 1);


fun g (x::y::z::rest) = x + y + z
|   g _ = 0;

fun h x =
    let
        val temp = 1;
    in
        temp + x
    end;
       