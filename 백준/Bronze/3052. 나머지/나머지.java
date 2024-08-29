import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int idx = 0;
        for(int i:arr){
            arr[idx] = sc.nextInt()%42;
                idx++;
        }
        int answer = 0;
        
        Arrays.sort(arr);
        idx = 0;
        for(int i:arr){
            switch (idx){
                case 0:
                    answer+=1;
                    break;
                default:
                    if(arr[idx]!=arr[idx-1]){answer+=1;}
                    break;
            }
                
            idx++;
        }
        
        System.out.println(answer);
    }
}