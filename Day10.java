import java.util.*;
import java.io.*;

class Day10 {
    public static void main(String[] args) throws Exception{
        Scanner scan = new Scanner(new File("day10.txt"));
        while(scan.hasNext()) {
            String str = scan.nextLine();
            String[] splitted = str.split(" ");
            System.out.println(splitted[0]);
            if(str.startsWith("value")) {
                int value = Integer.parseInt(splitted[1]);
                int botNr = Integer.parseInt(splitted[5]);
            } else {
                int botNr = Integer.parseInt(splitted[1]);
                int low = 
            }
        }
    }
}