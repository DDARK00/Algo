import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        String txt = sc.next();
        
        String txtArr[] = txt.split("");
        
        int leng = txt.length();
        //텍스트 전체의 길이
        
        String lengArr[] = {"ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"};
            //거리 배열
            //인덱스 +3 이 거리
        
        int t = 0;
        // 시간
        
        for (int i = 0 ; i<leng ; i++){
            // txtArr[i]는 현재 돌고 있는 문자
            for(int j = 0 ; j<lengArr.length;j++){
                //j는 거리 문자의 인덱스
                if(lengArr[j].contains(txtArr[i])){
                    t+=j+3;
                }
            }
        }
        System.out.println(t);
    }
}