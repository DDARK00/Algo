import java.util.Scanner;



public class Main {
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int N = sc.nextInt();
        
        
        int F = 0;
        int T = 0;
        
        // five three
        
        int cnt = -1;
        for(int i = 0; i<N/3+1;i++){
            //3키로가 0개일 때부터 계산
            int ab=N-(i*3);
            // 남은 무게
            //System.out.println(ab+"남은 무게");
            
            
            if(ab%5==0){

                int sum = i+(ab/5);
                //System.out.println(sum);
                if(cnt ==-1){
                    cnt = sum;
                }else if(cnt>sum){
                    cnt = sum;
                }

            }
            
            
            
        }

    
        
        
      System.out.println(cnt);
    }
}