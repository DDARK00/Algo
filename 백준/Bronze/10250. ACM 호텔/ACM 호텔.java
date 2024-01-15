import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        //테스트케이스 수
        
        for(int i = 0; i<T; i++){
        int H, W, N;
            H = sc.nextInt();
            //height 높이
            W = sc.nextInt();
            //width 너비
            N = sc.nextInt();
            //손님 수
            
            //무조건 1호실부터 배정
            // 6층 30번째  6 6 6 6 6  몫 5 +1  6층 5홓 605   6%5
            // 6층 10번째 6  4 402호 몫1 +1
            
            //30 50 72번째
            // 30 30 12 
            
            //층수 0이아니면 나머지
            //0이면 마지막
            
            //호실 몫 +1
            
            int floor = N%H==0?H:N%H;
            //층수
            
            int room = N%H==0?N/H:N/H+1;
            //방번호
            
            System.out.println(floor+""+(room<10?"0"+room:room));
                

            
        }
    }
}