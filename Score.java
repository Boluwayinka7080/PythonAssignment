import java.util.Scanner;
public class Score{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    System.out.print("Enter first score: ");
    int score1 = input.nextInt();

    System.out.print("Enter second score: ");
    int score2 = input.nextInt();

    System.out.print("Enter third score: ");
    int score3 = input.nextInt();

    int average = (score1 + score2 + score3) / 3;
    System.out.println("The average is " + average);

    
    

    if(90 <= average && average <= 100){
    System.out.print("Your grade is A ");
    }
    if(80 <= average && average < 90){
    System.out.print("Your grade is B ");
    }
    if(70 <= average && average < 80){
    System.out.print("Your grade is C "); 
    }
    if(60 <= average && average < 70){
    System.out.print("Your grade is D ");
    }
    if(0 <= average && average < 60){
    System.out.println("Your grade is F ");
    }











}






}
