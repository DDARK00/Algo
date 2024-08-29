import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //스트림 데이터를 버퍼 단위로 읽기
        
        int T = Integer.parseInt(br.readLine());
        //횟수(첫 줄) 버퍼에서 int로 변환
        
        for(int i = 0;i<T;i++){
            StringTokenizer lineInt = new StringTokenizer(br.readLine());
            //줄 단위로 읽어서 공백을 기준으로 split;
            
            bw.write(Integer.parseInt(lineInt.nextToken())+Integer.parseInt(lineInt.nextToken())+"\n");
            //다시 그 값을(string) int로 형변환
            
        }
        
        bw.close();
            //스트림 닫기
    }
}
// 스트림 데이터를 다룰 때는 exception 처리를 반드시 해야 한다...?