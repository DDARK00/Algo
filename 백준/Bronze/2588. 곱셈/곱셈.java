import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int a;
        String b;
        
        a = sc.nextInt();
        b = sc.nextInt()+"";
        int fir,sec,thr;
        fir = Integer.valueOf(b.substring(2,3));
        sec = Integer.valueOf(b.substring(1,2));
        thr = Integer.valueOf(b.substring(0,1));
        
        System.out.println(a*fir);
        System.out.println(a*sec);
        System.out.println(a*thr);
        System.out.println(a*Integer.valueOf(b));
    }
}