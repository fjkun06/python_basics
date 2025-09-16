games = ['ea fc26', 'pes6','cod 6', 'mario kart']
print(games[-4].title())
print(f'\nMy first game was {games[1]}\n')
games[2] = 're6'
print(games)
games.append('tlou2')
print(games)
games.insert(1,'minecraft')
print(games)

del games[1]
print(games)
popped_game=games.pop()
first_game=games.pop(0)
print(games)
print(popped_game, first_game)
re6 = 're6'
games.remove(re6)
print(games,re6)   