import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        
        int T = sc.nextInt();
        for(int i = T ; i>0;i--){
            System.out.println(" ".repeat(i-1)+"*".repeat(T-i+1));
        }
    }
}