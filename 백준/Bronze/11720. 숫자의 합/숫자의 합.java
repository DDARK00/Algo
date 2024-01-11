import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String word = sc.next();
        
        int sum = 0;
        
        for(int i = 0; i<n;i++){
            int s = word.charAt(i)-'0';
            // 아니 나 진짜 이해가 안 돼서 왜 하필 0을 빼는 거지
            // gpt한테 물어봤는데 0의 아스키 코드의 정수값을 빼면 정확한 정수값이 나온다고 한다
            // 숫자 0의 아스키 코드 값은 48이고, 0에서 0을 빼면(48-48) 0이 나온다는 것 같다...
            // 이게 쉽나...??????
            sum +=s;
        }
        System.out.println(sum);
    }
}