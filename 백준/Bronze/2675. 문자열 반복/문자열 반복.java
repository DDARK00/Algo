import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        //테스트케이스 사이클
        
        for(int i= 0; i<T;i++){
            
        int n = sc.nextInt();
        //문자 반복횟수
            
        String s = sc.next();
        
        String[] arr = s.split("");
        
        String answer = "";
        
            
        for(int j = 0;j<arr.length;j++){
            answer+=arr[j].repeat(n);
        }
        
        System.out.println(answer);
            
        }
        
    }
}