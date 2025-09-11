
abstract class Shape {
    int a, b;  
    Shape(int a, int b) {
        this.a = a;
        this.b = b;
    }

    abstract void printArea();
}

class Rectangle extends Shape {

    Rectangle(int length, int breadth) {
        super(length, breadth);
    }

    void printArea() {
        int area = a * b;
        System.out.println("Area of Rectangle: " + area);
    }
}

class Triangle extends Shape {

    Triangle(int base, int height) {
        super(base, height);
    }

    void printArea() {
        double area = 0.5 * a * b;
        System.out.println("Area of Triangle: " + area);
    }
}

class Circle extends Shape {

    Circle(int radius) {
        super(radius, 0);
    }

    void printArea() {
        double area = Math.PI * a * a;
        System.out.println("Area of Circle: " + area);
    }
public class Main {
    public static void main(String[] args) {
        Shape rectangle = new Rectangle(10, 5);
        rectangle.printArea();

        Shape triangle = new Triangle(8, 6);
        triangle.printArea();

        Shape circle = new Circle(7);
        circle.printArea();
    }
}
