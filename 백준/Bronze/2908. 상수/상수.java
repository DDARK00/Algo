import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String a,b;
        a = sc.next();
        b = sc.next();
        StringBuilder ap = new StringBuilder(a);
        StringBuilder bp = new StringBuilder(b);
        
        ap.reverse();
        bp.reverse();
        //이거 분명히 더 나은 방법이 있을 것 같은데 몰????루???????
        
        int app = Integer.parseInt(ap.toString());
        int bpp = Integer.parseInt(bp.toString());
        System.out.println(app>bpp?app:bpp);
    }
}