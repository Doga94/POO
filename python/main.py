from car import Car

if __name__ == "__main__":
    print("Hola mundo")
    car = Car()
    car.license = "sdw522"
    car.driver = "David"
    print(vars(car))

    car2 = Car()
    car2.license = "dse587"
    car2.driver = "Luisa"
    print(vars(car2))