'''
    Make a program that opens an audio.mp3
'''
import pygame
pygame.init()
pygame.mixer.music.load("type the song here.mp3")
pygame.mixer.music.play()
pygame.event.wait()
