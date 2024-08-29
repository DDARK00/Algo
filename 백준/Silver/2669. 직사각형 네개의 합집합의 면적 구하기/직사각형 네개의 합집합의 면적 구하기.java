import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        
        // 첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.

    
        //모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.
        int arr[][] = new int[100][100];
        
        for(int i = 0; i<4;i++){
            int xa = sc.nextInt(); //1
            int ya = sc.nextInt(); //2
            
            int xb = sc.nextInt(); //4
            int yb = sc.nextInt(); //4
            
            
            for(int j = xa; j<xb;j++){
                //가로로 채우기
                for(int l=ya;l<yb;l++){
                    //가로로 채우기를 세로로 반복하기
                    arr[j][l]= 1;
                    
                    
                }
                
            }
            
            
            
            
        }
        
    int cnt = 0;
    for(int ar[] : arr ){
        for(int a : ar){
            cnt+= a;
        }
    }
    
    System.out.println(cnt);
    }
}