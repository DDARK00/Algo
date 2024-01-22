import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int s, n;
        s = sc.nextInt();
        //과일의 수
        
        n = sc.nextInt();
        // 초기 스네이크의 길이
        
        int ar[] = new int[s];
        
        for(int i = 0 ; i<s;i++){
            ar[i] = sc.nextInt();
        }
        
        
        Arrays.sort(ar);
        
        for(int j = 0; j<s;j++){
            if(n>= ar[j]){
                n++;
                
            }else{
                break;
            }
        }
        System.out.println(n);
        //이거 이대로 맞으면 실버5가 아닌데...?
    }
}