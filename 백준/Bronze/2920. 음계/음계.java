import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        //일단 무조건 숫자 8개가 들어온다.
        int startInt = sc.nextInt();
        
        switch(startInt){
            case 1 :
                for(int i = 2 ; i<9;i++){
                    int targetInt = sc.nextInt();
                    if(i== targetInt){
                        if(i==8){
                        System.out.println("ascending");
                        break;
                        }
                        continue;
                        // 같으면 계속 진행
                    }else{
                    System.out.println("mixed");
                        //다르면 끝
                    break;
                    }
                }
                break;
            case 8:
                    for(int i = 7 ; i>0;i--){
                    int targetInt = sc.nextInt();
                    if(i== targetInt){
                        if(i==1){
                    System.out.println("descending");
                            break;
                        }
                        continue;
                        // 같으면 계속 진행
                    }else{
                    System.out.println("mixed");
                        //다르면 끝
                    break;
                    }
                }
                
                break;
            default:
                System.out.println("mixed");
                break;
        }
        
        
    }
}