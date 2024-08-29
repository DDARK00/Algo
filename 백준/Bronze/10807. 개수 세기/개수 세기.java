import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int[] arr = new int[size];
        for(int i = 0 ; i<size;i++){
            arr[i] = sc.nextInt();
        }
        
        
        int cnt = 0;
        int target = sc.nextInt();
                for(int i = 0 ; i<size;i++){
            cnt += arr[i] == target?1:0;
        }
        System.out.println(cnt);
    }
}