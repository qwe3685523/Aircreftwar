#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import pygame

hero_rect = pygame.Rect(100, 500, 50, 60)
print("英雄的原点%d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸%d %d" % (hero_rect.width, hero_rect.height))
print("英雄的尺寸%d %d" % hero_rect.size)