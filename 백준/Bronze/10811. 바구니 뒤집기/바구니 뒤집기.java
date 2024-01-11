import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int m, n;
        n = sc.nextInt();
        // 바구니의 수
        
        m = sc.nextInt();
        //바구니를 바꾸는 수
        
        int[] arr = new int[n];
        int idx = 0;
        for(int i : arr){
            arr[idx] = idx+1;
            idx++;
        }
        //1부터~~~ 세팅

        int st, ed;
                    String a = "";
        for(int i = 0 ; i<m;i++){
            st = sc.nextInt()-1;
            //1번은 인덱스0, m번 반복
            
            ed = sc.nextInt()-1;
            
            
            //int[] stack = new int[n];
            //int pointer = 0;
            //스택으로 할 수 있을것 같은데 구현 방법을 모르겠다!
            
            //1부터 4까지면
            // 1 2 3  4 sum 5
            // 1 4  5- 1 ; 2 3 5-2 ; 
            int cnt = (ed-st)/2+1;
            
            int save;

            // 1234567
            // 1 7 2 6 3 5 4 4
            // 234
            // 4번 sum 8
            // 
            // 3 45 
            for(int j =0;j<cnt;j++){

                save = arr[st+j];
                arr[st+j] = arr[ed-j];
                arr[ed-j] = save;
            }
        }
                        for(int k : arr){

                    a+=k+" ";
                }
            
        System.out.println(a.trim());
    }
}