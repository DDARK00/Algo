import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 들어오는 재료의 개수
        
        int m = sc.nextInt();
        // 필요한 재료의 수
        
        int ar[] = new int[n];
        
        for(int i = 0 ; i<n;i++){
            ar[i] = sc.nextInt();
        }
        
        // 투 포인터 입문
        // 정렬된 배열에 대하여(몇몇 케이스에서는 정렬 안 돼도 되나봄)
        Arrays.sort(ar);
        // 여담으로 어레이스의 sort는 이진 어쩌고 정렬이라 카더라
        
        int left, right;
        // 풀 때 나는 a, b 같이 썼는데 보기 편하게 right left로 했다.
        
        left = 0;
        right = n-1;
        // 방향은 같은 방향에서 출발하는 경우, 양 끝 방향에서 가운데로 모이는 경우가 있는데
        // 일단 하나...
        int cnt = 0;
        while(true){
            // 정렬이 되어 있으니까
            // 합이 m보다 크면 -1(right가 왼쪽으로)
            // 합이 m보다 작으면 +1(left가 오른쪽으로)
            // 합이 m과 같다면 cnt+1, left +1 , right -1(다음거 카운트)
            
            //가운데에서 두 포인터가 만나면 종료
            if(left >= right){
                // 만나면이라서 == 했다가 차이가 홀수개라 틀렸음 확실히 조건을 줘야 하는듯
                // 이래놓고 left>right 했다가 또 틀렸네 같거나 크다가 맞네 어휴
                // 그러고보니까 이거 while true가 아니어도 될 듯
                break;
            }
            
            int sum = ar[left]+ar[right];
            if(sum >m){
                right--;
            }
            
            if(sum <m){
                left++;
            }
            
            // 같으면
            if(sum == m ){
                left++;
                right--;
                cnt++;  
            }
            
            
        }
        
        System.out.println(cnt);
    }
}