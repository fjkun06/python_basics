from dog import Dog
from car import Car
from electric_car import ElectricCar

my_dog = Dog("Willie", 6)
my_dog.roll_over()

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading -= 23
my_new_car.read_odometer()
my_new_car.update_odometer(55)
my_new_car.read_odometer()

# inherited from car class
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
my_leaf.update_odometer(55)

my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()