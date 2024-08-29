import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int total = sc.nextInt();
        int T = sc.nextInt(); 
        for(int i=0; i<T;i++){
            int a = sc.nextInt();
                int b=sc.nextInt();
            total-=(a*b); 

        }
        System.out.println(total==0?"Yes":"No");
    }
}