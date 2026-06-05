package UntilIGetPlaced.GoAhead;
import java.util.Scanner;
public class Greatestofthreenumbers {
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the first number: "); 
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();
    int max=Math.max(a, Math.max(b, c));
    System.out.println("The greatest of three numbers is: "+max);
    
}
}