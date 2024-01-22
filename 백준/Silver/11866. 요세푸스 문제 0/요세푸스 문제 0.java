import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
// import java.util.ArrayList;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i = 0; i<n;i++){
            q.offer(i+1);
        }
        // ArrayList<String> answer = new ArrayList<>();
        String answer = "";
        
        while(true){
            Integer target;
            // k 앞의 수를 큐 맨 뒤로 이동,
            // k 를 빼서 버림
            // 반복
            
            for(int j = 1; j<k;j++){
                // 숫자는 1부터 시작;
                target = q.poll();
                q.offer(target);
            }
            
            target = q.poll();
            if(target == null){
                break;
            }
            answer+=", "+target;
            
        }
        
        
        System.out.println("<"+answer.substring(2)+">");
    }
}

// 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
// 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
// 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
// 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다. =