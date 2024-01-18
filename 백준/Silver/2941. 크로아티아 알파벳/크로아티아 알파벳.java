/*

č   c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=

*/

import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        
        String txt = sc.next();
        
        String cA[] = {"c=", "c-", "dz=", "d-", "lj" , "nj", "s=", "z="};
        
        int cnt = 0;
        
                // System.out.println(txt.indexOf(cA[4]));
                // System.out.println(txt.substring(0,0));
                //  System.out.println(txt.substring(0+cA[4].length()));


        for(int i = 0; i<8;i++){
            while(true){
                int idx = txt.indexOf(cA[i]);

                if(idx == -1){
                    break;
                }

                String forward = txt.substring(0,idx);
                
                String back = txt.substring(idx+cA[i].length());
                cnt++;
                txt = (forward+"x"+back);
                continue;
                
            }
        }
        // System.out.println(txt);

        System.out.println(txt.length());
    }
}