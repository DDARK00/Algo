import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a,b,c,d,e,f;
        
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        e = sc.nextInt();
        f = sc.nextInt();
           
           
           for(int x = -999;x<1000;x++){
               for(int y = -999;y<1000;y++){
                   
                   if((a*x+b*y==c)&&(d*x+e*y==f)){
                             System.out.println(x+" "+y);

                   }
                   
                   
               }
           }
           
           
           
    }
}