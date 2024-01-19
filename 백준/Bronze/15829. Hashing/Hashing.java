import java.util.Scanner;
import java.math.BigInteger;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        String[] abc = sc.next().split("");
        //BigInteger는 string으로 처리.,.,. 

        long M = 1234567891;
        
        BigInteger answer =  new BigInteger("0");
        
        for (int i = 0; i<T;i++){
            
            char c = abc[i].charAt(0);
            //한글자씩 받는다
            // a가 아스키코드 97, 96을 빼면 1이 됨
            
            int num = (int)c -96;
            
            //a * 31^i 를 더하면 되는듯?
            // for(int j = 0; j<=i;j++){
                BigInteger k = new BigInteger(num+"");
                
                k = k.multiply(new BigInteger("31").pow(i));
                BigInteger remain = k.remainder( new BigInteger(M+""));
                answer = answer.add(remain);
                // System.out.println(remain);
            // }
   
        }
        
        System.out.println(answer.remainder(new BigInteger(M+"")));
        
    }
}