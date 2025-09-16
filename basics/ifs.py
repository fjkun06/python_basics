cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    elif car == "toyota":
        print("I so love Japan!!")
    elif car == "sasa":
        print("I so nada")
    else:
        print(car.title())

# print(len(cars) != 40)

age_0 = 24
age_1 = 23

testx = age_0 >= 201 or age_1 >= 21 
print((age_0 and age_1))

requested_toppings = ["mushrooms", "onions", "pineapple"]
print('eggs' not in requested_toppings)
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
