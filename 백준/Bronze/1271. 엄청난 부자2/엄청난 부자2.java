import java.util.Scanner;
import java.math.BigInteger;

public class Main{
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        // BigInteger 문제... 당혹스러웠다
        
        BigInteger n = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        
        BigInteger d = n.divide(b);
        BigInteger m = n.remainder(b);
        
        System.out.println(d);
        System.out.println(m);
    }
}