user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

friends = ["phil", "sarah"]
# key-value destructurx
for key, value in user_0.items():
    print(f"{key}: {value}")

# key destructurx
for name in favorite_languages:
    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()} loves {language.title()}")

# value destructurx
for value in set(favorite_languages.values()):
    print(f"{value.title()}")
# print('lasts' in user_0.keys())

nx = ["1", 1, 5, 5, 7, 8, 7, 9, "9", "8"]
print(nx, len(nx))
mx = set(nx[:])
print(mx, len(mx))

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
 # Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")