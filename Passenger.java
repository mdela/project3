public class Passenger {
	
	// fields
	String name;
	int fare;
	int distance;
	
	// constructors
	public Passenger(String name, int distance, int fare) {
		this.name = name;
		this.fare = fare;
		this.distance = distance;
	}
	public Passenger(String name) {
		this.name = name;
	}
	
	// getters
	public String getName() {
		return name;
	}
	public int getFare() {
		return fare;
	}
	public int getDistance() {
		return distance;
	}
	
	// setters
	public void setName(String name) {
		this.name = name;
	}
	public void setFare(int fare) {
		this.fare = fare;
	}
	public void setDistance(int distance) {
		this.distance = distance;
	}
	
	// methods
	public void summary() {
		System.out.println("It will take " + distance + " miles to get to "
				+ name + "'s home. " + name + " owes you $" + fare);
	}
}
