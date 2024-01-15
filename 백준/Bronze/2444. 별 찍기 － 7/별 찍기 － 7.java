//import java.util.Scanner;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{
    public static void main(String args[]) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //선언
        
        String txt = br.readLine();
        int n = Integer.parseInt(txt);
        // input
        
        //input 5
        // 1 3 5 7 9
        // 10 - 9 10 - 7 10 - 5 10 - 3  10 - 1
        // 공백 4 3 2 1 0
            
        
        for(int i = n; i>0; i--){
           System.out.println(" ".repeat(i-1)+"*".repeat(2*n-2*i+1));
        }
        for(int j = 1; j<n; j++){
           System.out.println(" ".repeat(j)+"*".repeat(2*n-2*j-1));
        }
    }
}