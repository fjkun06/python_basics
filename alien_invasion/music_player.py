from pygame import mixer

#Background Sound
def play_music():
  """Play Music indefinitely"""
  mixer.music.load('sounds/Migos - Bad and Boujee ft Lil Uzi Vert [Official Video].wav')
  mixer.music.play(-1)
