import java.util.Scanner;


public class Main{
    public static void main(String args[]){
        
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        int maxM = 1;
        int minM = 1000001;
        int mAr[] = new int[T];
        for(int i = 0; i<T ; i++){
            int next = sc.nextInt();
            mAr[i] = next;
            if(maxM<next){
                maxM = next;
            }
            if(minM>next){
                minM = next;
            }
        }
        
        
       
        
        System.out.println(maxM*minM);
    }
}