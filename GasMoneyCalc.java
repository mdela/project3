import java.util.Scanner;

public class GasMoneyCalc {

	public static void main(String[] args) {
		
		// TODO
		// - refine the summary tab
		// - determine who gets dropped off in order
		// - add fees
	
		Scanner input = new Scanner(System.in);
		
		// declare variables
		int mpg;
		float gasPrice; 
		
		// gather input
		System.out.print("Enter the car's mpg: ");
		mpg = Integer.parseInt(input.nextLine());
		System.out.print("Enter the current price per gallon: ");
		gasPrice = Float.parseFloat(input.nextLine());
		
		// the goal is to calculate miles per dollar
		float milesPerDollar;
		milesPerDollar = Math.round(mpg / gasPrice);
		
		System.out.println(); // line break
		
		// gather passengers
		System.out.print("-- Add Passengers --");
		// create array of passengers, 4 max
		Passenger[] car = new Passenger[4];
		for (int i = 0; i < car.length; i++) {
			System.out.println();
			String name;
			int distance;
			int fare;
			
			System.out.print("Enter passenger name: ");
			name = input.next();
			if (name.equals("finish".toLowerCase())) {
				break;
			}
			
			System.out.print("Enter distance to passenger's home: ");
			distance = input.nextInt();
			
			// calculate how much the passenger has to pay
			fare = (int)(Math.ceil(distance / milesPerDollar));
			
			car[i] = new Passenger(name, distance, fare);
			System.out.println(car[i].getName() + " has been added.");
		}
		
		// summary tab
		System.out.println("\n-- Summary --");
		
		// print...
		System.out.println("MPG: " + mpg);
		System.out.println("Gas price: $" + gasPrice + " per gallon");
		System.out.println("Miles per dollar: " + milesPerDollar + "mi\n");

		
		for (int i = 0; i < car.length; i++) {
			if (car[i] == null) { break; }
			car[i].summary();
		}
				
	}

}
