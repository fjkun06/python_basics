def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
      print(f"- {topping}")
      
def count_pizza_toppings(*toppings):
  """
  Count the toppings on the pizza.
  """
  print(f"\nYour pizza has {len(toppings)}-toppings :)")
    