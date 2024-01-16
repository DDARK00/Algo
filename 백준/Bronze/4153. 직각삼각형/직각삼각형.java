import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int a, b, c;

        while(true){
            a = sc.nextInt();
            b = sc.nextInt();
            c = sc.nextInt();
            
            if(a == 0 && b == 0 && c == 0){
                break;
            }
             int pa, pb, pc;

            pa = a*a;
            pb = b*b;
            pc = c*c;

            int arr[] = new int[3];
            if(pa>pb){
                arr[0] = pb>pc?pc:pb;
                arr[1] = pb>pc?pb:pc;
                arr[2] = pa>pc?pa:pb;
            }else if(pb>pc){
                //pa가 pb보다 작거나 같을 때
                arr[0] = pc>pa?pa:pc;
                arr[1] = pc>pa?pc:pa;
                arr[2] = pa>pb?pa:pb; 
            }else{
                //pc가 제일 클 때
                arr[2] = pc;
                arr[1] = pa>pb?pa:pb;
                arr[0] = pa>pb?pb:pa;
            }
            // 아 그냥 sort 쓸 걸 그랬나
            
            if(
            arr[2] ==arr[1]+arr[0]
                ){
                System.out.println("right");
            }else{
                System.out.println("wrong");
                
            }
            
        }
    }
}