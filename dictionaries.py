aline = {'color':'green', 'points':5}

print(aline['color'])

aline['skin'] = 'brown'

aline['eyelash'] = 'black'

print(aline)

aline["skin"] = "dodgerblue"
aline["skins"] = ["dodgerblue",'gray','jawohl']
del aline['color']
print(aline)
for key in aline:
  print(key)
