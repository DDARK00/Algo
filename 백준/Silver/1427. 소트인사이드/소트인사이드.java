import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        
        String arrS[] = S.split("");
        
        int arrI[] = new int[arrS.length];
        int idx = 0;
        for(String i : arrS){
            arrI[idx] = Integer.parseInt(i);
                idx++;
        }
        Arrays.sort(arrI);
        String ans = "";
        for(int j = arrI.length;j>0;j-- ){
            ans+=(arrI[j-1]+"");
        }
        System.out.println(ans);
    }
}