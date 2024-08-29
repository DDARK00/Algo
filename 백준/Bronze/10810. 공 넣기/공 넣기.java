import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int basketN = sc.nextInt();
        //바구니의 수
        
        int T = sc.nextInt();
        //시행 사이클
        
        int arr[] = new int[basketN];
            int st,ed,target;
        //시작,끝, 바꿀 값
        for(int i=0 ; i<T;i++){
            st = sc.nextInt()-1;
            ed = sc.nextInt();
            target = sc.nextInt();
            for(int j = st; j<ed;j++ ){
                // j 가 스타트부터 ed까지
                arr[j] = target;
            }
        }
        
        String answer = "";
        for(int k = 0 ; k<basketN;k++){
            answer+=" "+arr[k];
        }
        System.out.println(answer.trim());
    }
}