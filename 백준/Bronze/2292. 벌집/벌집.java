import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        //1은 1
        //6각형
        //2~7   6개 2칸
        //8~19  18개 12개 3칸   3    3
        //20~37 36개 18개 4칸   6    4
        //38~61 60개 24개 5칸   10
        
        //첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.
        
        //   37 3칸 5 6 + 12 + 18 3칸 5    36  6 
        
        //  13 3
        
        int N = sc.nextInt();
        
        if(N==1){
        System.out.println(1);
        }else if(N<8){
        System.out.println(2);

        }else{
            

        N -=2;
        int sum = 0;
        
         for(int i = 1; i<N;i++){
             
             sum+=i*6;
             if(sum>N){
                 System.out.println(i+1);
                 //시작,끝점 
                 break;
             }
         }
                }
    }
}