import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        
        //a 오르는 양
        //b 내려가는 양
        //c 올라가야 하는 양
        
        if(a>=c){
            System.out.println(1);
        }else{
            // 1일에 끝남
        
            //-----------//
            int dayUp = a - b;  
            
            
            int dPlus = (c-a)%dayUp != 0 ?2:1;
            System.out.println((c-a)/dayUp +dPlus);
            //
            }
    }
}