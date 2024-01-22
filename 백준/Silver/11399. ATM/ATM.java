import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int time[] = new int[N];
        
        for(int i = 0 ; i<N ;i++){
            time[i] = sc.nextInt();
        }
        
        // 그리디 : 현 상황에서 최적의 판단 ex)지폐 거스름돈
        // 사람 줄이기 -> 시간 줄이기, 기다리는 사람에 비례해서 증가함ㅇㅇ;
        
        Arrays.sort(time);
        
        int sum = 0;
        for(int j = 0 ; j<N ;j++){
            sum += time[j] * (N-(j+1));
            sum+=time[j];

            // 남은 사람의 수만큼 시간이 늘어남
        }
        
        System.out.println(sum);
        
    }
}