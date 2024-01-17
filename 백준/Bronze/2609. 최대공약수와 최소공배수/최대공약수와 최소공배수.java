//첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();
        
        int pa = a;
        int pb = b;


        while(true){
            if(pa==pb){
                
                break;
            }
            //24 18
            if(pa<pb){
                
                pa+=a;
                continue;
            }else{
                pb+=b;
                continue;
            }

        }
        
        System.out.println((a*b)/pa);
        System.out.println(pa);
    }
}