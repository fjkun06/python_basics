from pygame import mixer
import pygame

# Background Sound
# class MusicPlayer:
#   """Music Player Media Controller"""

#   def __init__(self):
#     """Kickstart media player"""
playlist = [
    "sounds/Migos - Bad and Boujee ft Lil Uzi Vert [Official Video].wav",
    "sounds/Migos, Nicki Minaj, Cardi B - MotorSport (Official Video).wav",
    "sounds/Niykee Heaton - Bad Intentions ft. Migos.wav",
]


def music_player(playlist_index):
    """Play Music indefinitely"""
    mixer.init()
    music_index = 0
    music_index += playlist_index
    mixer.music.load(playlist[music_index])
    pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Event when song ends
    mixer.music.play(-1)

    # playing = True

    # Pause music
    # _control_playback()
    # while playing:
    #   for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_SPACE:
    #             pygame.mixer.music.pause()
    #             print(f"{event.key} clicked")


# music_player(current_index)
def _update_player(index):
    """Perform calculations to locate the right song"""
    music_player(index % len(playlist))


def media_player(playing):
    """Control all music ops"""
    current_index = 0

    # Startr playing Music
    music_player(current_index)

    # Pause music
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                current_index += 1
                _update_player(current_index)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    current_index -= 1
                    _update_player(current_index)
                elif event.key == pygame.K_d:
                    current_index += 1
                    _update_player(current_index)


# music_player(current_index)


def _control_playback():
    """Control the Music playback"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.pause()


def _play():
    """Play/Resume the Music playback"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.pause()


def _pause():
    """Play/Resume the Music playback"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mixer.music.pause()
