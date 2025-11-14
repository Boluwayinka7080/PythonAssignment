import java.util.Scanner;
public class Calculator{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    
    System.out.println("Enter two numbers:");
    double figure1 = input.nextDouble();

    System.out.println("Input first number:");
    double figure2 = input.nextDouble();

    System.out.println("Input operator(+, -, *, /):");
    String operator = input.next();


    String plus = "+";
    String minus = "-";
    String divide = "/";
    String multiply = "*";


     double sum = figure1 + figure2;

     double subtract = figure1 - figure2;
    
     double multiplication = figure1 * figure2;
    
     double division = figure1 / figure2;
    

    if(operator.equals( "+")){
    System.out.println("The sum of the numbers is " + sum);
    }
    if(operator.equals("-")){
    System.out.println("The difference of the number is " + subtract);
    }
    if(operator.equals("/")){
    System.out.println("The division of both numbers is " + division);
    }
    if(operator.equals("*")){
    System.out.println("The multiplication of both numbers is " + multiplication);
    }



}



}
