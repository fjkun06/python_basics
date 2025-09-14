def greet_user(username):
    """Display a simple greeting."""
    print(f'Hello, {username.title()}')


def describe_pet(pet_name, pet_type="wolf"):
    """Display info about a pet."""
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.\n")

# describe_pet('harry')
# describe_pet(pet_name='potter', pet_type='human')

def get_formatted_name(first_name,last_name):
    """Return formatted name."""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

def build_person(first_name, last_name):
    """Return Dictionary of person."""
    person = {'first':first_name,'last':last_name}
    return person

# magicial = get_formatted_name('frank','jordan')
# magician = build_person("frank", "jordan")
# print(magicial, magician)

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_design(unfinished_designs,printed_models):
    """
       Simulate printing each design, until none are left.
       Move each design to completed_models after printing.
    """
    while unfinished_designs:
        curr_design = unfinished_designs.pop()
        print(f"Printing model: {curr_design}")
        printed_models.append(curr_design)

def showcase_models(models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in models:
        print(model)

print_design(unprinted_designs, completed_models)
showcase_models(completed_models)
