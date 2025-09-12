magicians = ["alice", "bob", "patrick"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}\n")
# print("Thank you everyone. That was a great show.")
comp_magicians = [magician + '-kun' for magician in magicians]
print(comp_magicians)
numbers = list(range(-11,9))
# print(numbers)
# for x in range(1,6):
#     print(x)

print(numbers)
comp_numbers = [value**2 for value in numbers]
print(min(numbers),max(numbers),sum(numbers))
print(comp_numbers)


players = ["charles", "martina","jack", "michael", "florence", "eli"]
first_three_players = players[:3]
print(f'Here are the first {len(first_three_players)} players on my team:')
for player in first_three_players:
    print(player.title())
