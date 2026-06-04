package UntilIGetPlaced.GoAhead;
import java.util.Scanner;
public class AmstrongNumber {
    public static void main(String[] args){
    System.out.println("Enter the number: ");
    Scanner sc = new Scanner(System.in);
    int n=sc.nextInt();
    int sum=0;
    int temp=n;

    while(n!=0){
        int digit=n%10;
        sum+=digit*digit*digit;
        n/=10;
    }
    if(temp==sum){
        System.out.println("Amstrong number");
    }else{  
        System.out.println("Not an Amstrong number");
    }
    
}
}