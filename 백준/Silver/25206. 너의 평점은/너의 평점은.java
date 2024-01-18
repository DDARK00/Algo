import java.util.Scanner;
import java.util.Arrays;

//20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

//string string?double? string
//과목명 //학점 //등급

//등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        
        String n, g, d;
        int cnt = 0;
        double sum = 0;
        
        String gd[] = {"F","X","D0","D+","C0","C+","B0","B+","A0","A+"};
        //0  1  2 3 4 5 6 7 8 9 * 0.5
        for(int i = 0; i<20;i++){
            n = sc.next();
            g = sc.next();
            d = sc.next();
            
            // System.out.print(n+" "+g+" "+d+"\n");
            
            if(!d.equals("P") ){
                cnt+=Integer.parseInt(g.substring(0,1));
                
                sum += (Arrays.asList(gd).indexOf(d)*0.5) * (Integer.parseInt(g.substring(0,1)));
                // System.out.println(Arrays.asList(gd).indexOf(d)*0.5);
                // System.out.println(Integer.parseInt(g.substring(0,1)));

                
            }
            
        }
        
                    System.out.print(sum/cnt);

    }
}
