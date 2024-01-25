import java.io.*;

public class Main {
    public static void main(String args[])throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        // 테케 수
        
        
        // N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
        
        int table[][] = new int[41][2];
        // 테이블의 최대 크기
        
        // 초기
        // 0의 수 1의 수
        table[0][0] = 1;
        table[0][1] = 0;
        
        table[1][0] = 0;
        table[1][1] = 1;
        
        
        
        for(int i = 2; i<41;i++){
            table[i][0] = table[i-1][0] + table[i-2][0];
            // 
            table[i][1] = table[i-1][1] + table[i-2][1];
            //
        }
        // 점화식 복붙했는데
        // 이거 문제에 써진거 보고 그대로 옮겼는데 왜 이게 맞는지 모르겠거든?????
        // DP 입문 문제인가?
        
        
        
        for(int i = 0; i<T;i++){
            int n = Integer.parseInt(br.readLine());
            // 구하고자 하는 수
            System.out.println(table[n][0]+" "+table[n][1]);
            
        }
    }

}