package java;
class Main{
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Car car = new Car();
        car.license = "jmr233";
        car.driver = "Ivan";
        car.passenger = 4;
        car.printDataCar();
    }
}