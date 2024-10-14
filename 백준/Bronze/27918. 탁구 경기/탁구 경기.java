import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());

        int p = 0;
        int d = 0;
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            if (s.equals("P") ){
                p+=1;
            }else{
                d+=1;
            }
            if (Math.abs(p-d) == 2) break;
        }
        
        bw.write(d + ":" + p);
        
        bw.flush();
        bw.close();
    }
}
