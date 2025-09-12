players = ["charles", "martina", "jack", "michael", "florence", "eli"]
first_three_players = players[:3]
print(f"Here are the first {len(first_three_players)} players on my team:")
for player in first_three_players:
    print(player.title())


fav_foods= ['ripe plantains','steak and bobolo','garri and eru']
bros_fav_foods = fav_foods[:]
fav_foods.append('mekoum')
bros_fav_foods.append('rice and beans')
print(fav_foods,bros_fav_foods)