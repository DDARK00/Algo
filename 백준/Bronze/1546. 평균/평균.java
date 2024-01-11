import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int max=0 ;
        
        for(int i = 0; i<n;i++){
            int nowScore = sc.nextInt();
            max=max<nowScore?nowScore:max;
            arr[i]=nowScore;
        }
        double sum = 0;
        for(double j : arr){
            sum+=(j/max)*100;
        }
        
        System.out.println(sum/n);
        
    }
}