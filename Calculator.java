import java.util.Scanner;
public class Calculator{
    public static void main(String[] args){
    Scanner input = new SCanner(System.in);
    
    System.out.print("Enter two numbers");
    double figures = input.nextDouble();

    System.out.print("Input first number");
    double figure1 = input.nextDouble();

    System.out.print("Input second number");
    double figure2 = input.nextDouble();

    String plus = "+";
    String minus = "-";
    String divide = "/";
    String multiply = "*";


     double sum = figure1 + figure2;

     double subtract = figure1 - figure2;
    
     double multiplication = figure1 * figure2;
    
     double division = figure1 / figure2;
    
    System.out.print("What do you want to do ?");
    if("+"){
    System.out.print("The sum of the numbers is " + sum);
    }
    if("-"){
    System.out.print("The difference of the number is " + subract);
    }
    if("/"){
    System.out.print("The division of both numbers is " + division);
    }
    if("*"){
    System.out.print("The multiplication of both numbers is " + multiplication);
    }



}



}
