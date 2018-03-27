#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import pygame

# 初始化pygame的所有模块
pygame.init()
# 游戏逻辑
# 创建游戏窗口
# set_mode（(),） 三个参数  第一个参数resolution（窗口的宽和高）flag附加参数  depth  颜色的位数
# 400 * 700
window = pygame.display.set_mode((480, 700))
# 添加图像文件
#       1加载图片
#       pygame.image.load(path)
#       2添加图片
#         blit（图像,位置/矩形）
#       3刷新
#         pygame.display.update()
bg = pygame.image.load("./images/background.png")
window.blit(bg, (0, 0))
pygame.display.update()
# 游戏循环
while True:
    pass
# 卸载所有的Pygame模块
pygame.quit()
