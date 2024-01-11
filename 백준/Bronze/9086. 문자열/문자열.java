import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        int leng;
        for (int i=0;i <T ; i++){
        String txt = sc.next();
            leng = txt.length();
        String arr[] = txt.split("");
                       
            
            
        System.out.println(arr[0]+""+arr[leng-1]+"");
        }
        
        
    }
}