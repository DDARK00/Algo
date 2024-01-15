import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        String[] abc = sc.next().split("");
        
        int L = 26;
        int M = 1234567891;
        
        int answer = 0;
        
        for (int i = 0; i<T;i++){
            
            char c = abc[i].charAt(0);
            //한글자씩 받는다
            // a가 아스키코드 97, 96을 빼면 1이 됨
            
            int num = (int)c -96;
            
            //a * 31^i 를 더하면 되는듯?
            
            answer+=(num*(Math.pow(31,i)));
                    

            
        }
        
        System.out.println(answer);
        
    }
}