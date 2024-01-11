# -*- coding: cp1252 -*-
"""
    Copyright (C) 2017 - Instituto Federal de Educacao, Ciencia e Tecnologia do Sul de Minas Gerais, Muzambinho
    Author: Diego Penha - diego.penha95@gmail.com


    This file is part of As Aventuras de Dude no Mundo Top-Down.

    As Aventuras de Dude no Mundo Top-Down is free software:
    you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    As Aventuras de Dude no Mundo Top-Down
    is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with As Aventuras de Dude no Mundo Top-Down.
    If not, see <http://www.gnu.org/licenses/>.
"""
import pygame
import Configs as Cfg
from random import randint


# Ammo object
class ammobox(pygame.sprite.Sprite):
    def __init__(self, spriteA):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteA
        self.sizeX = pygame.Surface.get_width(self.image)
        self.sizeY = pygame.Surface.get_height(self.image)
        self.X = randint(Cfg.LARGURA / 4, Cfg.LARGURA - Cfg.LARGURA / 4)
        self.Y = randint(self.sizeY, Cfg.ALTURA - self.sizeY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.bonusAmmo = Cfg.BONUS_AMMO

    def changePos(self):
        self.X = randint(self.sizeX, Cfg.LARGURA - 44)
        self.Y = randint(self.sizeY, Cfg.ALTURA - 44)
        self.rect.topleft = (self.X, self.Y)


# Health object
class Health(pygame.sprite.Sprite):
    def __init__(self, spriteH):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteH
        self.sizeX = pygame.Surface.get_width(self.image)
        self.sizeY = pygame.Surface.get_height(self.image)
        self.X = randint(Cfg.LARGURA / 4, Cfg.LARGURA - Cfg.LARGURA / 4)
        self.Y = randint(self.sizeY, Cfg.ALTURA - self.sizeY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.bonusHP = Cfg.BONUS_HEALTH

    def changePos(self):
        self.X = randint(self.sizeX, Cfg.LARGURA - 44)
        self.Y = randint(self.sizeY, Cfg.ALTURA - 44)
        self.rect.topleft = (self.X, self.Y)


# Points object
class Points(pygame.sprite.Sprite):
    def __init__(self, spritePTS):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritePTS
        self.sizeX = pygame.Surface.get_width(self.image)
        self.sizeY = pygame.Surface.get_height(self.image)
        self.X = randint(Cfg.LARGURA / 4, Cfg.LARGURA - Cfg.LARGURA / 4)
        self.Y = randint(self.sizeY, Cfg.ALTURA - self.sizeY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.bonusPts = Cfg.BONUS_POINTS

    def changePos(self):
        self.X = randint(self.sizeX, Cfg.LARGURA - 44)
        self.Y = randint(self.sizeY, Cfg.ALTURA - 44)
        self.rect.topleft = (self.X, self.Y)


# Shield object
class Shield(pygame.sprite.Sprite):
    def __init__(self, spriteSh):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSh
        self.sizeX = pygame.Surface.get_width(self.image)
        self.sizeY = pygame.Surface.get_height(self.image)
        self.X = randint(Cfg.LARGURA / 4, Cfg.LARGURA - Cfg.LARGURA / 4)
        self.Y = randint(self.sizeY, Cfg.ALTURA - self.sizeY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.shieldTime = Cfg.SHIELD_TIME

    def changePos(self):
        self.X = randint(self.sizeX, Cfg.LARGURA - 44)
        self.Y = randint(self.sizeY, Cfg.ALTURA - 44)
        self.rect.topleft = (self.X, self.Y)
