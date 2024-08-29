import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        
        for( int i = 0; i < T ; i++ ){
            String ox = sc.next();
            if(!ox.contains("O")){
                System.out.println(0);
                continue;}
            String oxArr[] = ox.split("");
            
            int score = 0;
            //라운드점수
            
            
            int now = 0;
            //현재점수
            
            for( int j = 0; j < oxArr.length ; j++ ){
               if(oxArr[j].equals("X"))continue;
                if(j != 0 && oxArr[j-1].equals("O")){
                    now+=1;
                    }else{
                    now = 1;
                    }
                score+=now;
                }
            
               
               System.out.println(score+"");
            }
             //폰으로 하기 너무 힘들다;;
        }
    }