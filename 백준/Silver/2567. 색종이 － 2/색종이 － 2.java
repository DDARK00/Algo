import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        int arr[][] = new int[101][101];
        for (int k=0; k<n; k++) {
            String[] str = br.readLine().split(" ");
            int a = Integer.parseInt(str[0]);
            int b = Integer.parseInt(str[1]);
            for (int i = a; i < a+10; i++) {
                for (int j = b; j<b+10; j++) {
                    arr[i][j] = 1;
                }
            }
        }
        
        int sums = 0;
        int dx[] = {0,0,1,-1};
        int dy[] = {1,-1,0,0};
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (arr[i][j]==1) {
                    for (int d=0; d<4; d++) {
                        int nx = i+dx[d];
                        int ny = j+dy[d];
                        if (0<=nx && 0<=ny &&arr[nx][ny]==0) {
                            sums+=1;
                        }
                    }
                    
                }
            }
        }
        bw.write(Integer.toString(sums));
        bw.flush();
        bw.close();
    }
}