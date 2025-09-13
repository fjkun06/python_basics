# basic while loop
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# interactive while loop
prompt = "\n Tell me something sweet, then I'll fall for you:"
prompt += "\nEnter 'quit' to end the program. "

# basic flag
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         # active = False
#         break
#     else:
#         print(message)

# filling dictionary
responses = {}
name_prompt = '\n What is your name? '
res_prompt = 'Which mountain would you like to climb someday? '
continue_prompt = 'Would you like to let another person respond? (yes/ no) '
# gettting user response
prompt_active = True
while prompt_active:
    name = input(name_prompt)
    response = input(res_prompt)

    # adding input to dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    continuing = input(continue_prompt)
    if continuing == 'no':
      prompt_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")