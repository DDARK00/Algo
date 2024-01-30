import java.util.Scanner;
import java.lang.Math;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int c =sc.nextInt(); 
        int k = sc.nextInt();
        
        
        System.out.println((int)(Math.round(c/Math.pow(10,k))*Math.pow(10,k) ));
    }
}