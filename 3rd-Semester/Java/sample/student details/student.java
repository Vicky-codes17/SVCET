//Printing the Students Details 
class student
{
	int Roll_No;
	int Age;
	void display()
	{
		System.out.println("Roll No is " +Roll_No);
		System.out.println("Age is " +Age);
	}
}
class sample
{
	public static void main(String args[])
	{
		student s1 = new student();
		student s2 = new student();
		s1.Age = 18;
		s1.Roll_No = 1;
		s2.Age = 18;
		s2.Roll_No = 2;
		s1.display();
		s2.display();
	}
}