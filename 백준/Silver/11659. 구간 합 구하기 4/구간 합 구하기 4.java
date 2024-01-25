import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        //첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 
        int n = sc.nextInt();
        // 개수
        
        int m = sc.nextInt();
        // 횟수
        
        int nar[] = new int[n];
        //n 넣을 배열
        
        for(int i =0; i<n;i++){
            nar[i] = sc.nextInt();
        }
        
        
        int newar[] = new int[n+1];
        // 누적 합산 배열
        newar[0] = 0;
        newar[1] = nar[0];
        // 초깃값 정의
        // 아 여기가 좀 애매한데 일단 0번인덱스를 0으로 잡고 1번부터 들어온다고 하고
        
        
        for(int i = 2 ; i<n+1;i++){
            newar[i] = newar[i-1]+nar[i-1];
            // 이게 점화식이니?
            // 인덱스가 1만큼 차이나니까 보정해 주고(nar) 2부터 +1까지~
            
        }
        
        // for(int i : newar){
        //     System.out.println(i);
        // }
        
        // answer는  a부터 b까지
        //  b까지의 합 빼기 a 앞까지의 합
        
        for(int i = 0 ; i<m;i++){
            int a = sc.nextInt(); //앞
            int b = sc.nextInt(); //뒤
            // System.out.println(a+" "+b);
            a = a-1 <0 ?0 :a-1;
            System.out.println(newar[b]-newar[a]);
            // System.out.println(newar[a]);
            // 1 3 -> 5 + 4 + 3 ->  15 - 2
            // 뒤 빼기 앞

            
        }
        // 이거 그냥 인덱스 조정 안하고 a가 인덱스 벗어났을 때의 예외처리가 더 나았을지도 모르겠다?
      
    }
}