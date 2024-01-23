import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        // 1~99 까지는 각 수가 한수
        
        if(T<100){
             System.out.println(T);
             return;
        }
        int cnt = 99;
        if(T==1000){
            T = 999;
            //1000은 한수가 아님... 빼고한다...
        }
        for (int i = 100; i<=T;i++){
            // 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
            
            //3자리의 수가 들어오면
            
            int third = i%10; //일의자리
            int second = (i/10)%10 ; //십의자리  230 23 3 
            int first = i/100; //백의자리  1 4 7    7 4 1      
            
            if((third - second)==(second-first)){
                cnt++;
            // System.out.println(i);
            }
            
            
            
            
        }
        System.out.println(cnt);
    }
}