import java.util.Scanner;
import java.util.StringTokenizer;

public class Main{
    public static void main(String args[]){

        Scanner sc = new Scanner(System.in);
        String txt = sc.nextLine();
        /*        
        String arr[] = txt.trim().split(" ");
        if(arr[0].isEmpty()){
        System.out.println("0");    
        }else{
        System.out.println(arr.length);
            }
        
        */
        
        StringTokenizer st = new StringTokenizer(txt);
        System.out.println(st.countTokens());
        
    }
}