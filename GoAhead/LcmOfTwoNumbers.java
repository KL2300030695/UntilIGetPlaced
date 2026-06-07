package UntilIGetPlaced.GoAhead;
import java.util.Scanner;
public class LcmOfTwoNumbers {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number: "); 
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();
        int lcm=(a>b)?a:b;
        while(true){
            if(lcm%a==0 && lcm%b==0){
                System.out.println("The LCM of two numbers is: "+lcm);
                break;
            }
            lcm++;
        }
    }
    
}
