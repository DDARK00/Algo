import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int arr[] = new int[30];
        
        for(int i = 0 ; i<28;i++){
            arr[sc.nextInt()-1] = 1;
        }
        
        for(int j = 0 ; j<30;j++){

            if(arr[j]==0){
                System.out.println(j+1);
            }
        }
    }
}