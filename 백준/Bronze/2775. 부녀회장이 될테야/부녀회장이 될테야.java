import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        
        for(int cycle = 0; cycle < T; cycle++){
            int a, b;
            a = sc.nextInt();
            b = sc.nextInt();
            //a는층 b는 호실 호실은 1부터 시작;;;
            
            //아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
            // int cnt = 0;
            // if(a==0){
            //     //0층이면 예외처리?
            //     for(int j = 1; j<b; j++){
            //         cnt+=j;
            //     }
            //     System.out.println(cnt);
            //     continue;
            // }
            
            //a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
            
            
            //0층이 아니면
            
            // a 1 층  101호
            // 0층의 1호1 
            // a 1 층 의 102 호
            // 0 층의 1 호1  2 호2
            
            // arr[k][l] = arr[k-1][l]+arr[k-1][l-1]...
            
            // 2층의 202호   4 203호 8  202호는 arr[1][1] + arr[1][2]...    203호는arr[1][0]+ arr[1][1]+ arr[1][2] + arr[1][3]  이라고 생각했는데......
            // 이게아니라 arr[2][2]+ arr[1][3]
            // 1층 101 1 102 3 103 6
            // 0층 101 1 102 2 103 3
            
            int arr[][] = new int[a+1][b+1];
            
            arr[0][1] = 1;
            arr[0][0] = 0;
            for(int k = 1; k<=b; k++){
                arr[0][k] = k;
                //초기값 정의
            }
            
            // DP로 해보자
            for(int i = 1 ; i <=a; i++){
                for(int j =1; j<=b; j++){
                    arr[i][j] = arr[i][j-1]+arr[i-1][j];
                    
                    
                }
            }
            
            // System.out.println(arr[a][b]);
            System.out.println(arr[a][b]);
            
            
        }
    }
}