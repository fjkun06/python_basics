first_name = '  frank      '
last_name = 'jordan'
full_name = f'{first_name.title().strip()} {last_name}'
# print(f'\tHello, \n\t\t{full_name}')

#Exercises

person_name = 'Madhaus Frank'
message = f'\nHello {person_name}, would you like to learn some Python today?\n'
print(message)
message = f'Result:\n\tlowercase: {person_name.lower()}, \n\tuppercase: {person_name.upper()}, \n\tcapitalize: {person_name.title()}\n'
print(message)
quote= 'A person who never made a mistake never \ntried anything new.'
quote_message = f'{person_name} once said, "{quote}"\n'
print(quote_message)
suffix_name = 'python_notes.txt'
print(suffix_name.removesuffix('.txt'))
