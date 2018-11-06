"""
1.把静止的图像绘制到游戏窗口
2.根据用户交互，移动图像产生动画效果
3.根据图像之间是否发生重叠，判断敌机是否被摧毁
"""

import pygame

pygame.init()  # 初始化pygame模块
hero_rect = pygame.Rect(200, 500, 102, 126)  # 矩形区域 四元组（left, top , width, height）

'''
print('坐标原点：（{}，{}），尺寸（宽，高）：{}'.format(hero_rect.x,
                                       hero_rect.y,
                                       hero_rect.size))
'''

screen = pygame.display.set_mode((480, 700))  # 初始化显示窗口，返回屏幕对象
# 游戏元素图像的绘制基于返回的屏幕对象

bg = pygame.image.load('images/background.png')  # 加载图像数据，Surface对象
hero = pygame.image.load('images/me1.png')

screen.blit(bg, (0, 0))  # 将图像加载到屏幕指定位置
screen.blit(hero, (200, 500))

pygame.display.update()  # 刷新屏幕对象显示

clock = pygame.time.Clock()  # 游戏时钟：设置刷新帧数  ---  帧是每秒绘制的次数

i = 0
while True:  # 游戏无限循环
    clock.tick(60)  # 每秒循环刷新60次，达到动画效果
    # i += 1
    # print(i)
    hero_rect.y -= 2              # 移动效果的实现
    if -hero_rect.height > hero_rect.y:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)   # 利用背景覆盖原来的游戏元素
    pygame.display.update()


pygame.quit()  # 卸载pygame模块
