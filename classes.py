from dog import Dog
from car import Car

my_dog = Dog("Willie", 6)
my_dog.roll_over()

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading -= 23
my_new_car.read_odometer()
my_new_car.update_odometer(55)
my_new_car.read_odometer()
