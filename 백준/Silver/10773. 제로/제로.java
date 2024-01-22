import java.util.Stack;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        Stack<Integer> st = new Stack<>();
        // 큐는 linkedlist로 하는데 스택은 그냥 뉴 스택이다
        // LILO
        
        // 스택 기초인거 같은데 이거 바닐라로 어떻게 만들어?
        for(int i =0;i<T;i++){
            
            int target = sc.nextInt();
            
            if(target != 0){
            st.push(target);
            }else{
                st.pop();
            }
            
            
        }
        int sum = 0;
        while (true){
            if(st.empty())break;
            
            sum+= st.pop();
            
        }
        
        
        System.out.println(sum);
    }
}