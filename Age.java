import java.util.Scanner;
public class Age{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter fathers current age: ");
    int fatherAge = input.nextInt();

    System.out.print("Enter sons age: ");
    int sonAge = input.nextInt();

     int numberOfYears = (2 * sonAge) - fatherAge;

    System.out.println("in" + numberOfYears + "years the father will be twice as old as his son"); 








}




}
