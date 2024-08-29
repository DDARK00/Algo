import java.io.*;
import java.util.Queue;
import java.util.LinkedList; 

// 큐 기본 실습
// 자바에서의 큐는 LinkedList를 이용해서 구현하나 보다.

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        Queue<Integer> q = new LinkedList<>();
        // 제네릭 인티저
        
        // 값 추가는 q.add 아니면 q.offer로 하는데,
        // 둘의 기능적 차이는 없고 추가에 실패시 add는 IllegalStateException, offer는 false를 반환한다
        
        for(int i = 0; i<n;i++){
            q.offer(i+1);
        }
        
        // q.poll 첫번째 값 반환하고 제거, 값이 없으면 null
        // q.remove 첫번째 값 제거
        // q.clear 큐 초기화
        
        // q.peek() 첫번째 값 참조만 함(조회)
        
        
        
        // 문제
        //  N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다.
        //  3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.
        //  맨 앞에 하나 빼고 다음꺼 맨 뒤로
        
        String answer = "";
        while(true){
            Integer first = q.poll();
            Integer second = q.poll();
            //  여기서 재밌는게, int타입은 null을 받을 수 없어서 에러가 뜨더라
            //Integer는 null도 받을 수 있다고 한다
            
            if(first==null){
                break;
            }
            
            answer+= first+" ";
            q.offer(second);
            
            
        }
        System.out.println(answer);
    }
}