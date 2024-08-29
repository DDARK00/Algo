import java.io.*;
import java.math.BigInteger;

public class Main{
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if(n==0){
            System.out.println("0");
            return;
        }
        if(n==1){
            System.out.println("1");
            return;
        }
        
        BigInteger dp[] = new BigInteger[n+1];
        // BigInteger 문제였나...
        // 0 1 1 2 3 5 8 13 21 34 55
        // 0 1 2 3 4 5 6  7  8  9 10
        dp[0] = new BigInteger("0");
        dp[1] = new BigInteger("1");
        for(int i = 2; i<n+1;i++){
            dp[i] = dp[i-1].add(dp[i-2]);
        }
        
        System.out.println(dp[n]);
        
    }
}