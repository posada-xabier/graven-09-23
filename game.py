import pygame
from player import Player

class Game():
    def __init__(self):
        self.player = Player()
        # dico avec les keys actives = pressed down
        # "touche fleche droite" : Try
        self.pressed = {}
    