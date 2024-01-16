import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String target;
        while (true){
            target = sc.next();
            if(target.equals("0")){
                break;
            }
            String[] arr = target.split("");
            
            int len = arr.length-1;
            if(len == 0){
                System.out.println("yes");
                continue;
            }
                //인풋이 한자리면 
            
            boolean tf = true;
            //나머지는 맞는다고 가정?
            
            for(int i=0;i<len/2+1;i++){
                if(arr[i].equals(arr[len-i])){
                    continue;
                }else{
                    tf=false;
                    break;
                }
            }
            if(tf){
            System.out.println("yes");    
            }else{
            System.out.println("no");

            }

        }
    }
}