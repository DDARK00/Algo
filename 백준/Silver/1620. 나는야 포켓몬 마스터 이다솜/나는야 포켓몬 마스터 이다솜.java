import java.util.Scanner;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Set;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        // 들어오는 포켓몬의 수
        
        int m = sc.nextInt();
        // 맞혀야 하는 문제의 수
        
        
        // String p[] = new String[n];
        HashMap<Integer, String> hm = new HashMap<>();
        HashMap<String,Integer> hm2 = new HashMap<>();
        
        for(int i = 0; i<n;i++){
            // p[i] = sc.next();
            String pName = sc.next();
            hm.put(i+1,pName);
            hm2.put(pName,i+1);
        }
        
        Set<Integer> keys = hm.keySet();
   
        for(int j = 0; j<m;j++){
            String a = sc.next();
            try{
                Integer target = Integer.parseInt(a);
                System.out.println(hm.get(target));
                
            }catch(NumberFormatException e){
                // 이름이 들어오면
                System.out.println(hm2.get(a));
            }
            
        }
        
        // 이렇게 하라고 준 문제는 아닌 것 같지만 풀리지 않을까
        // 해시맵 두 개...
    }
}