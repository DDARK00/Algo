import java.util.Scanner;

public class Main{
    public static void main(String args[]){
Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        
        for(int i = 0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        int index = 0;
        int save;
        
        for( int j = n; j>0;j--){
            
        
            for(int i =0 ; i<j-1;i++){
                if(arr[i]>arr[i+1]){
                    save = arr[i];
                    arr[i] =  arr[i+1];
                    arr[i+1] = save;
                }
            //1회전 버블정렬
            }
        }
        for(int k : arr){
            
        System.out.println(k);
            //와 이게 한방에 됐네 
        }
        
    }
}