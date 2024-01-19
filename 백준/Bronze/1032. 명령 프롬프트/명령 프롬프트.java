import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        String N[] = new String[T];
        
        for(int i = 0; i<T;i++){
            N[i] = sc.next();
        }
        
        String answer = "";
        //파일 이름의 길이는 모두 같고 ... 최대 파일 길이만큼 탐색
        for(int j = 0; j<N[0].length();j++){
            //0번째가 같은가
            
            // T[0].substring(j,j+1) 첫 파일명의 j번째 글자가 나머지와 같은가?
            // 아 이거 또 메모리나 시간 초과 아님?
            
            String target = N[0].substring(j,j+1);
            // System.out.println(target);
            for(int l = 1;l<=T; l++){
                if(l == T){
                    answer+=target;
                    break;
                }
                String s= N[l].substring(j,j+1);
                // System.out.println(s+"이것은SSS");
                // System.out.println(target.equals(s));

                if(!target.equals(s)){
                    answer+="?";
                    break;
                }
            }
            
            
            
        }
      System.out.println(answer);
    }
}