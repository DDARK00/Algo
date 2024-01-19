import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        int answer = 0;
        
        for(int i = 0; i<T;i++){
            String word = sc.next();
            // 단어 하나가 들어오면
            if(word.length()==1){
                answer++;
                continue;
            }
            
            String [] origin = word.split("");
            //원래 단어
            
            String [] wArr = new String[origin.length];
            //중복 체크로 스트링을 넣자... 
            
            String now = origin[0];
            //첫 단어 들고 시작하자...
            
            int index = 0;
            
            
            
            for(int j = 1; j<=origin.length;j++){
                // 1번이 0번이랑 같으면...으로 해야겠다
                
                // 1번이 0번이랑 다르면 0번을 wArr에 넣는다
                
                
                // 마지막까지 돌아서 들어오면 -> origin.length == j
                // 마지막 글자가 배열에 있는지 체크 + 없으면 answer++
                // 이 아니라 aaaa 처음 글자랑 마지막 글자가 같으면
                if(j==origin.length){
                    
                    if(Arrays.asList(wArr).indexOf(origin[j-1])== -1){
                        
                    // System.out.println(j);
                    
                    answer++;
                    break;
                    }else{
                        break;
                    }
                }
                
                
                if(!origin[j].equals(origin[j-1])){
                    // 다르면 -> 배열에 없으면 넣는다.
                    
                    int idx = Arrays.asList(wArr).indexOf(origin[j-1]);
                    // idx가 -1이면 없다
                    
                    if(idx== -1){
                        wArr[index] = origin[j-1];
                        index++;
                    }else{
                        //있으면
                        break;
                    }
                    
                    
                    
                }else{
                    //같으면 -> 다음 단어로 gogo
                    continue;
                }
                
                // System.out.println(origin[j]);
                // System.out.println(origin[j+1]);
                
                

            }
            
            // for( String k : wArr){
            //                     System.out.println(k);

            // }

            
        }
        
        System.out.println(answer);
    }
}