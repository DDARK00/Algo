import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String txt = sc.next();
        String ans = "";
        for(int i = 97;i<123;i++){
            char s = (char)i;
            int idx= txt.indexOf(s);
            ans+=(" "+idx);
        }
        System.out.println(ans.trim());
    }
}