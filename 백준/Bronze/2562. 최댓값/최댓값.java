import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int idx,target,now;
        idx = 0;
        target = 0;
        for(int i =0;i<9;i++){
            now = sc.nextInt();
            if(now>target){
                target= now;
                idx = i+1;
            }
        }
        
        System.out.println(target);
        System.out.println(idx);
    }
}