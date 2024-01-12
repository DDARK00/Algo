import java.util.Scanner;

import java.lang.Math;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        int cnt = 0;
        
        
        for(int i = 0 ; i<T;i++){
            // T만큼 반복
            
            
            int target = sc.nextInt();
            
            
            
            //--------------------------
            /*
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
            
             boolean isP = true;
             //소수인가? 소수라고 가정
            
             for (int j = 3; j<halfLine;j+=2){
                 //짝수면 패쓰
                 if(target%j==0){
                     isP = false;
                     break;
                     //나눠지면 끝
                 }
             }
            
            if(isP) cnt++;
        */
           //-----------------------------------
        //이하 찾아보고 만든 로직
            if(target == 1)continue;
            if(target ==2){
                cnt++;
                continue;
            }
            
            if(target%2==0)continue;
            boolean isPri = true;
            
            int cutLine = (int) Math.sqrt(target);
            // 제곱근까지만 a*b가 성립 어쩌고 증명은 몰러...
            // 실수 캐스팅
            for(int k=3; k<=cutLine;k+=2){
                //커트라인도 포함, 약수에도 존재하게 되어 있대...
                if(target%k==0){
                    isPri = false;
                    break;
                }
            }
            
            cnt +=isPri?1:0;
            
            
        }
        

        
        
        
        System.out.println(cnt);
    }
}