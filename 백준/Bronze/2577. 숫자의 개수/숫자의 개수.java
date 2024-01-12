import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int a, b, c;
        a = sc.nextInt();
        b  = sc.nextInt();
        c = sc.nextInt();
        
        int cross = a*b*c;
        
        String[] Tx = Integer.toString(cross).split("");
        
        int arr[] = new int[10];
        
        for(String i : Tx){
            int idx = Integer.parseInt(i);
            arr[idx] +=1;
        }
        
        for(int j : arr){
            System.out.println(j);
        }
    }
}