import java.util.Scanner;

public class Main{
    public static void main(String[] argggss){
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        
        System.out.println((year%4==0)&& 
                           ((year%400==0)||(year%100!=0))
                            
                            ?"1":"0");
    }
}