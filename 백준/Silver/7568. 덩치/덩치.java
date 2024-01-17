import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);

        int T = sc.nextInt();
        int[][] ar = new int[T][2];
        for(int cb = 0; cb<T;cb++){
            
            
            ar[cb][0] = sc.nextInt();
            //키
            ar[cb][1] = sc.nextInt();
            //몸무게
        }
        
        
//나보다 확실히 큰 개체가 얼마나 있는가???
        
        int rank = 1;
        String answer ="";
        int cnt = 0;
        
        for(int i = 0; i<T;i++){
            for(int j= 0; j<T; j++){



                
                if((ar[i][0]<ar[j][0])&&(ar[i][1]<ar[j][1])){
                        rank++;
                    }
                    
                    
                if(j==T-1){
                    answer+=rank+" ";
                    rank=1;
                }

            
            
            }
        }
        
        System.out.println(answer.trim());
        
    }
}