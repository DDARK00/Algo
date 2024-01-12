import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        int cnt = 0;
        
        for(int i = 0 ; i<T;i++){
            // T만큼 반복
            
            int target = sc.nextInt();
            if(target == 1) continue;
            //1이면 돌아감
            if(target ==2){
                cnt++;
                continue;
            }
            if(target%2==0) continue;
            int halfLine = target/2;
            //그 수의 절반 이상인 숫자는 약수가 될 수 없었나...?
            // 이거 루트 어쩌고 해서 최단평가 하는거 어디서 봤는데 기억이 안 난다
            
             boolean isN = true;
            //소수인가? 소수라고 가정
            
            
             for (int j = 3; j<halfLine;j+=2){
                 //짝수면 패쓰
                 if(target%j==0){
                     isN = false;
                     break;
                     //나눠지면 끝
                 }
             }
            
            if(isN) cnt++;
            
        }
        
        //-----------------------------------
        
        System.out.println(cnt);
    }
}