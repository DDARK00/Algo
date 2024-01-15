import java.util.Scanner;
import java.util.Arrays;
//단, 대문자와 소문자를 구분하지 않는다.

public class Main{
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String txt =sc.next();
        txt = txt.toUpperCase();
        // 모르겠는데 일단 통일
        
        String [] txtArr = txt.split("");
        Arrays.sort(txtArr);
        
        boolean tf = false;
        //같은 숫
    
        String answer = txtArr[0];
        //맨 앞 글자가 가장 많이 나왔다고 가정
        
        int cnt = 1;
        // 맨 앞거 하나
        int highCnt = 1;
        // 가장 높은거

        for(int i = 1; i<txtArr.length;i++){
            if(txtArr[i].equals(txtArr[i-1])){
                            

                //1번이 0번이랑 같으면 cnt+1
                cnt++;
                
                if(cnt>highCnt){
                    highCnt = cnt;
                    answer = txtArr[i];
                    tf = false;
                    // 현재 cnt가 더 높아지면 false
                }else if(cnt == highCnt){
                    tf = true;
                    //같으면 일단 트루
                }
            }else{
                if(cnt==1 &&highCnt==1 ){
                    tf= true;
                }else{
                    cnt = 1;
                }
            }
        }
        
                
                
        if(tf){
            System.out.println("?");
        }else{
            System.out.println(answer);

        }
    }
}