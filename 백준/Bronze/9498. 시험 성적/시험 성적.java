import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
        String degree;
        if(score>89){
            degree = "A";
        }else if(score>79){
            degree = "B";
        }else if(score>69){
            degree = "C";
        }else if (score>59){
            degree = "D";
        }else{
            degree = "F";
        }
        
        
        System.out.println(degree);
      
    }
}