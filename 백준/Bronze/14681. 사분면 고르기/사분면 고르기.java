import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int x = sc.nextInt();
        int y = sc.nextInt();
        int quad;
        
        if(x*y>0){
            quad= x<0?3:1;
            System.out.println(quad);
        }else if(x*y<0){
            quad = x>y? 4:2;
            System.out.println(quad);
        }
        
    }
}