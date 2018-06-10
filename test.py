#!/usr/bin/env python
# encoding: utf-8
import pygame, sys

pygame.init()
screen = pygame.display.set_caption('hello world!')
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
