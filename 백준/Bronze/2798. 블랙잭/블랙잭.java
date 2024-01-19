import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc =new Scanner(System.in);
        int N, M;
        N = sc.nextInt();
        // 카드의 개수
        
        M = sc.nextInt();
        // 최대 수
        
        
        // 최대한 가까운 카드 3장의 합
        
        int arr[] = new int[N];
        
        for(int i = 0; i<N;i++){
            arr[i] = sc.nextInt();
            //일단 숫자 다 받아서
        }
        
        
        // 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
        int f,s,t;

        //브루투포스인데 3중포문 감당 되나
        
        int answer = 0;
        int sum;
        for( f= 0; f<N;f++ ){
            for( s = f+1;s<N;s++){
                for( t = s+1; t<N; t++){
                    sum =arr[f] + arr[s] + arr[t];
                    
                    if((sum)<M+1){
                        if(sum>answer) answer = sum;
                    }
                }
            }
        }
        
        // 아 브루트포스 진짜 재밌다
        
      System.out.println(answer);
    }
}