package UntilIGetPlaced.GoAhead;
import java.util.Scanner;
public class GcdOFTwoNumbers {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number: "); 
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();
        while(a!=b){
            if(a>b){
                a=a-b;
            }
            else{
                b=b-a;
            }
        }
        System.out.println("The GCD of two numbers is: "+a);
    }
    
}
