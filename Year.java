import java.util.Scanner;
public class Year{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.println("Enter the number of days in the year:");
    int numberOfDays = input.nextInt();

    if(numberOfDays % 4 == 0 && numberOfDays % 100 != 0 && numberOfDays % 400 != 0) {
        System.out.println("This is a leap year");
    }
    else{
        System.out.println("This is not a leap year");    
    }






}




}
