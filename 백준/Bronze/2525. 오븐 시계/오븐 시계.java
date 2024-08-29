import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt(); //23
        int m = sc.nextInt(); //48
        m += sc.nextInt(); //73
        
        h+= m/60; //24
        m = m%60; //13
        h = h%24; //0
        
        System.out.println(h + " " + m);
        
        
    }
}