import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        
        Integer o_ar [] = new Integer[8];
        int new_ar[] = new int[8];
        
        int sum = 0;
        for(int i = 0; i<8;i++){
            int target =  sc.nextInt();
            o_ar[i] = target;
            new_ar[i] = target;
            sum+= target;
            
        }
        
        Arrays.sort(new_ar);
        
        sum-= (new_ar[0]+new_ar[1]+new_ar[2]);
        
        
        
        
        
        System.out.println(sum);
        int numar[] = new int[5];
        
        for(int j =3;j<8;j++){
            int idx = Arrays.asList(o_ar).indexOf(new_ar[j]);
            //이 아무것도 아닌 것에 한참 머리를 싸맸는데 처음 배열 선언할 때 int로 하면 -1이 나오고 Integer로 선언하면 값이 정상적으로 나온다...
            // 기본기가 부족했다.
            numar[j-3] = idx+1;

            
        }
        Arrays.sort(numar);
        
        for( int n : numar){
            System.out.print(n+" ");
        }
    }
}