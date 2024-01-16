import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        String t = sc.next();
        String ta[] = t.split("");
                        

        for(int i = 0; i<=ta.length/2;i++){
            if(ta[i].equals(ta[ta.length-1-i])){
                
                if(i==ta.length/2){
                System.out.println("1");

                }else{
                continue;    
                }
                
                
            }else{
                System.out.println("0");
                break;
            }
        }
        
        
    }
}