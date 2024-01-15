import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        boolean arr[] = new boolean[2000001];

        // 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다.
        // 수는 중복되지 않는다.
        
        for(int k = 0; k<T;k++){
            int target = Integer.parseInt(br.readLine());
            target += 1000000;
            arr[target] = true;
        }
        
        // 굉장히 재밌는 발상이라고 생각한다...

        StringBuilder ans = new StringBuilder();
        
        for(int i = 0;i<2000001;i++){
            if(arr[i]){
                ans.append((i-1000000)+"\n");
            }
        }
        
                        System.out.println(ans);

    }
}