import java.util.Set;
import java.util.Scanner;
import java.util.HashSet;
import java.util.Arrays;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        // Set<Integer> set = new Set<>();
        // set은 인터페이스라서 직접 구현이 불가능하다.
        
        Set<Integer> set = new HashSet<>();
        // hashset이나 treeset 등 구현클래스를 선택해서 인스턴스를 초기화한다.
        
        for(int i = 0; i<T; i++){
            set.add(sc.nextInt());
        }
        
        Integer arr[] = set.toArray(new Integer[0]);
        // 인티저의 배열을 0으로 하면... [0]은 참조값일 뿐 자동으로 배열의 크기를 조정해 준다...
        // 수동으로 설정할 수도 있기는 함 ㅇㅇ
        Arrays.sort(arr);
        for(int j= 0; j<arr.length;j++){
            System.out.print(arr[j]+" ");
        }
    }
}