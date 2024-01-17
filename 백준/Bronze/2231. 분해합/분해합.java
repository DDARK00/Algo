import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        int target = sc.nextInt();
        
        //자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
        
        for(int i = 0 ;i <=target; i++){
            // int leng = (i+"").toString().length();
            int sum = 0;



            // target이 10의 자리가 넘으면
            // 10의 자리를 분리해서 더한다
            // target 의 length가 2 이상
            int saved=i;
            
            while(true){

                sum+= saved%10;
                
                if(saved/10 ==0){
                    break;
                }
                
                saved = saved/10;
                
            }
            
            sum +=i;
            
            if(sum == target){
                System.out.println(i);
                break;
            }
            
            if(i == target){
            System.out.println(0);
            break;

            }
            
        }
        
        
    
    }
}