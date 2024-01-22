import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        
        // 23
        // 64 32 32     32      16   16    16  8   16   4   4  16   4   2   2        16   4  2  1  
        
        //  64   32  32     32  
        
        
        // 48        64    32  32     32   16  16        32  16 
        
        // 1 1 1 1 1 1 1 
        // 1 2 4 8 16 32 64
        
        // 1 0 0 0 0 0 0
        
        // 23 
        // 0 0 1 0 1 1 1 4개
        
        
        // 32
        // 0 1 0 0 0 0 0
        // 0 1 0 0 0 0 0     1개
        
        // 48 
        // 0 1 1 0 0 0 0
        //  32 + 16       2개
        
        // 머리로는 이해를 하겠거든??? 구현을 못 하겠네???
        
        // 이진수의 1의 수인데???
        // 내가 자바를 모른다???
        
        
        //  32        2 2 2 2 2 2 2
        
        int cnt = 0;
        while(true){
            if(x%2 == 1){
                cnt++;
            }
            if(x==1){
                break;
            }
            x /=2 ;
        }
        
        // 바로 이진수로 받는건 못하나?
        
        System.out.println(cnt);
    }
}