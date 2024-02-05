import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        int sta[] = new int[t];
        
        for(int i = 0; i<t ; i++){
            sta[i] = sc.nextInt();
            // 계단
        }
        if(t<3){
        int sum=0;
        for(int i =0; i<t; i++){
            sum+=sta[i];
        }
        System.out.println(sum);
        // 예외처리
        return;
        }
        
        int dp[] = new int[t];
        
        dp[0] = sta[0]; 
        dp[1] = sta[1]+sta[0];
        dp[2] = sta[2]+ Math.max(sta[0], sta[1]);
        
        // 마지막 계단은 반드시 밟음
        // 시작점은 계단x
        
        // 마지막 -1 or -2
        // -1 이면 -2   -2면 -1 -2
        
        // -1 -2로 -3같음  -2면 -3 or -4 3이든4든 -2에서 열려있음
        
        // 결국 1 2 3 4계단에서 4계단을 마지막으로 밟는 경우는
        // 124 134 둘 중 하나임
        // 그럼 1 2 3 4 5 6 7
        // 124 134  
        // 457 467
        // 밖에 없음
        // 이걸 점화식으로 나타내면
        // n[7] = Math.max(n[5], n[4]+6번계단 점수) + 7번점수
        // 한 페이즈 앞 점수 + 마지막 계단 점수
        // 머리터지겠네ㅋㅋ 바로 안 나온다
        
        for(int i = 3; i<t; i++){
            
        dp[i] = Math.max(dp[i-3]+sta[i-1], dp[i-2])+sta[i];
        
        
        }
        
        System.out.println(dp[t-1]);
    }
}