class Shape
{  
    void draw()
    {
        System.out.println("creating Shape...");
    }  
}  
class Square extends Shape
{  
    void draw()
    {
        System.out.println("creating square...");
    }  
}  
class Triangle extends Shape
{  
    void draw()
    {
        System.out.println("creating triangle...");
    }  
}  
class Pentagon extends Shape
{  
    void draw()
    {
        System.out.println("creating pentagon...");
    }  
}  
class TestRunTimePolymorphism
{  
    public static void main(String args[])
    {  
        Shape s;  
        s=new Shape(); // Creating Shape object
        s.draw(); 
        s=new Square();  // Creating square object
        s.draw();  
        s=new Triangle();  // Creating Triangle object
        s.draw();  
        s=new Pentagon(); // Creating Pentagon object 
        s.draw();  
    }     
}  
