import java.io.*;

public class Main{
    public static void main(String args[] ) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String txt =br.readLine();
        int n = Integer.parseInt(txt);
        
        for(int i = 1;i<n+1;i ++){
        System.out.println(i);
            }
        }
    }