//import java.util.Scanner;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.lang.Math;

public class Main{
    public static void main(String args[]) throws IOException{
//        Scanner sc = new Scanner(System.in);
//        int target = sc.nextInt();        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int target = Integer.parseInt(br.readLine());
        int cnt=0;
        int start = 1 ;


        //이렇게 하는게 맞는지 모르겠다
            
/*
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
*/
            
        //DP 초급편이래 이게...
        //머리가 못 따라가...
        //이걸 보고 어떻게 DP구나 아는 거지...
            
            
        //10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.
            
        // 1. 테이블 정의
        // 2. 점화식 찾기
        // 3. 초기값 정하기
        
        // 1. 테이블 : 
        
            int dpTable[] = new int[target+1];
        
        // 2. 점화식 찾기
            
        // 10 9 3 1      9 3 1        12 4 3 1
        
        // dpTable [10] = dpTable[9] +1 = dpTable[3]+2 = dpTable[1] +3
        // dpTable [12] = dpTable[4] +1 = dpTable[3]+2 = dpTable[1] +3
        // dpTable [12] = dpTable[8] +1 = dpTable[4] +2 = dpTable[2] +3 = dpTable[1]+1
        // dpTable [12] = dpTable[11] +1 = dpTable[]
        
        // dpTable[k] = dpTable[k/3] +1
        // dpTable[k] = dpTable[k/2] +1
        // dpTable[k] = dpTable[k-1]+1
        
        //그래서 이걸 어떻게 써먹어??????
        
        //3. 초기값 정의하기
        
        dpTable[0] = 0;
        dpTable[1] = 0;
        //1번째는 횟수 0으로 1이 된다
        
        //
            
            for(int i = 2; i<=target;i++){
                
                dpTable[i] = dpTable[i-1]+1;
                //for문에 들어왔다면 횟수는 1부터 시작한다.
                //재귀로 활용????하지 않고 테이블을 미리 만들어둔다, 테이블 조회가 재귀처럼 움직이네 이거
                //3이나 2로 나누어지지 않으면 다음 i로 ;
                
                if(i%3==0){
                    //3으로 나누어지는 경우
                    dpTable[i]=Math.min(dpTable[i],dpTable[i/3]+1);
                    //3으로 나눠지는 경우 중에서 -1, 2로 나누는 경우
                }
                
                if(i%2==0){
                    //2로 나누어지는 경우
                    dpTable[i]=Math.min(dpTable[i],dpTable[i/2]+1);
                    //2로 나눠지는 경우 중에서 -1, 3으로 나누는 경우
                }
            }


        //dp에도 방법이 많은거 같은데 내 머리로 가능한게 일단 for문밖에 없다;;;
        System.out.println(dpTable[target]);
    }
}