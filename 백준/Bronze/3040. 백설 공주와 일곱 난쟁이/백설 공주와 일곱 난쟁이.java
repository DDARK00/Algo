import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        //인풋은 9개

        int arr[] = new int[9];
        int sum = -100;
        for(int k = 0;k<9;k++ ){
            int target = sc.nextInt();
            arr[k] = target;
            sum+= target;
        }
        //초과분
        int a=0;
        int b=0;
        
        for(int i = 0; i<9;i++){
            //9 마리 중 7 마리는 100;
            for(int j= 1;j<9;j++){
                if(i==j)continue;
                if(arr[i]+arr[j]==sum){
                    a = i;
                    b = j;
                    // System.out.println(i+" "+j);
                    break;
                }
            }
             
        }
        
        for(int m = 0; m<9;m++){
            if(m==a || m==b){
                continue;
            }
            
            System.out.println(arr[m]);
        }

        //이렇게 하는게 맞냐...
        
    }
}