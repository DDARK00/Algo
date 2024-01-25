import java.io.*;

public class Main {
    public static void main(String args[])throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        long s = Long.parseLong(br.readLine());
        
        
        long idx=1;
        long cnt=0;
        while(true){
            if(s-idx<0){
                
                // cnt++;
                break;
            }
            s -= idx;
            idx++;
            cnt++;
            
        }
        System.out.println(cnt);
    }
}