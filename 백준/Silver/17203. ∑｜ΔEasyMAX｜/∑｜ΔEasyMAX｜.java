import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String args[]) throws IOException {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int q = sc.nextInt();
    //   n배열의 크기, 박자가 몇 개
    
    // q 문제의 수
      int [] arr = new int[n];
      
      for(int i = 0; i<n; i++){
          arr[i] = sc.nextInt();
      }
      
      
      int artable[] = new int[n+1];
      artable[0] = 0;
      
    //   구간합
      for(int i = 1; i<n;i++){
          if(arr[i]>arr[i-1]){
            artable[i] = artable[i-1]+arr[i] - arr[i-1];

          }else{
              
          artable[i] = artable[i-1]+ arr[i-1]- arr[i];
          }
      }

      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      for(int i = 0; i<q;i++){
         int a = sc.nextInt();
         int b = sc.nextInt();
         
         int ans = artable[b-1]-artable[a-1];

        bw.write(ans+"\n");
      }
    //   for(int i : artable){
    //       System.out.println(i);
    //   }
      
      bw.flush();
      bw.close();
      
      
      
    }
}
