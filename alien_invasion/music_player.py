from pygame import mixer
import pygame
import sys

# Background Sound
playlist = [
    "sounds/Migos - Bad and Boujee ft Lil Uzi Vert [Official Video].wav",
    "sounds/Migos, Nicki Minaj, Cardi B - MotorSport (Official Video).wav",
    "sounds/Niykee Heaton - Bad Intentions ft. Migos.wav",
]


def music_player(playlist_index):
    """Play Music indefinitely"""
    mixer.init()
    mixer.music.load(playlist[playlist_index])
    pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Event when song ends
    mixer.music.play(-1)


def _update_player(index):
    """Perform calculations to locate the right song"""
    music_player(index % len(playlist))


def media_player(ai_game,event):
    """Control all music ops"""
    # Pause music
    # for event in pygame.event.get():
    # if event.type == pygame.QUIT:
    #     sys.exit()
    if event.type == pygame.USEREVENT:
        ai_game.current_index += 1
        _update_player(ai_game.current_index)

    elif event.type == pygame.KEYDOWN:
        _play_pause_toggle(event)
        _next_previous_toggle(event, ai_game)


def _play_pause_toggle(event):
    """Play/Pause the Music playback"""
    if event.key == pygame.K_SPACE:
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()


def _next_previous_toggle(event, ai_game):
    """Next/Backward the Music playback"""
    if event.key == pygame.K_a:
        ai_game.current_index -= 1
        _update_player(ai_game.current_index)
    elif event.key == pygame.K_d:
        ai_game.current_index += 1
        _update_player(ai_game.current_index)
