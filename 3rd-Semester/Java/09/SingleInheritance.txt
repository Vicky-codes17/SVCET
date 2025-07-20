class Employee //Super class
{
	void salary() 
	{
        	System.out.println("Salary= 200000");
    	}
}
	// Sub class
class Programmer extends Employee 
{ 
	// Programmer class inherits from Employee class of extends keyword
    	void bonus() 
	{
        	System.out.println("Bonus=50000");
    	}
}
class SingleInheritance 
{
	public static void main(String args[]) 
	{
        	Programmer p = new Programmer();
        	p.salary(); // calls method of super class
        	p.bonus(); // calls method of sub class
    }
}
