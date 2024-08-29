import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int repeat = sc.nextInt();
        String txt = "long ";
        
        System.out.println(txt.repeat(repeat/4)+"int");
    }
}