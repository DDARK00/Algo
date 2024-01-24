import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Arrays;


public class Main {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        // 듣 수
        
        int M = sc.nextInt();
        // 보 수
        
        
        Set<String> noHear = new HashSet<>();
        Set<String> noSee = new HashSet<>();
        
        
        for(int i = 0 ; i< N; i++){
            noHear.add(sc.next());
        }
        for(int j = 0; j<M; j++){
            noSee.add(sc.next());
        }
        noHear.retainAll(noSee);
        String[] humans = noHear.toArray(new String[0]);
        // O(N)
        Arrays.sort(humans);
        
        System.out.println(noHear.size());
        for(String human : humans){
            System.out.println(human);
        }
        // 되냐...
    }
}