package java;
class Main{
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Car car = new Car("jmr233", new Account("David", "Dav587"));
        car.passenger = 4;
        car.printDataCar();
    }
}