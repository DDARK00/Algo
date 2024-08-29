import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n,x;
        n = sc.nextInt();
        x = sc.nextInt();
        String answer = "";
        int[] arr = new int[n];
        for(int i = 0 ; i<n;i++){
            int now = sc.nextInt();
            if(now<x){
                answer += now+" ";
            }
        }
        System.out.println(answer.trim());
    }
}