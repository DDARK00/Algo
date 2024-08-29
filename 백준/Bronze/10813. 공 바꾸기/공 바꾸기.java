import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int arrSize = sc.nextInt();
        int[] arr = new int[arrSize];
        
        int changeCnt = sc.nextInt();
        
        for(int i = 0 ; i<arrSize;i++){
            arr[i] = i+1;
        }
        int a, 
        b, c;
        
        for(int j = 0; j<changeCnt;j++){
            a = sc.nextInt();
            b = sc.nextInt();
            
            c = arr[a-1];
            arr[a-1] = arr[b-1];
            arr[b-1] = c;
        }
        String ans = "";
        for(int k = 0 ; k<arrSize; k++){
            ans+= arr[k]+" ";
        }
        System.out.println(ans.trim());
    }
}