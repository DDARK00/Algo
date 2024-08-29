import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        
        if(m-45<0){
            m +=15;
            h-=1;
            h = h<0?23:h;
        System.out.println(h+" "+m);        
        }else{
         m-=45;
            System.out.println(h+" "+m);
        }
        
    }
}
