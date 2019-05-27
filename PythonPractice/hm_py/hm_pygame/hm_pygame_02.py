"""

事件（event）：针对游戏所做的操作（点击关闭按钮，鼠标，键盘）
监听：捕获用户具体操作，做出针对响应

精灵，精灵组
"""

from plane_sprites import *
import pygame

pygame.init()  # 初始化pygame模块
hero_rect = pygame.Rect(200, 500, 102, 126)  # 矩形区域 四元组（left, top , width, height）

screen = pygame.display.set_mode((480, 700))  # 初始化显示窗口，返回屏幕对象
# 游戏元素图像的绘制基于返回的屏幕对象

bg = pygame.image.load('images/background.png')  # 加载图像数据，Surface对象
hero = pygame.image.load('images/me1.png')

screen.blit(bg, (0, 0))  # 将图像加载到屏幕指定位置
screen.blit(hero, (200, 500))

pygame.display.update()  # 刷新屏幕对象显示

clock = pygame.time.Clock()  # 游戏时钟：设置刷新帧数  ---  帧是每秒绘制的次数

enemy1 = GameSprite('images/enemy1.png')
enemy2 = GameSprite('images/enemy1.png', 2)
enemy_group = pygame.sprite.Group(enemy1, enemy2)  # 创建精灵组

while True:  # 游戏无限循环
    clock.tick(60)  # 每秒循环刷新60次，达到动画效果

    event_list = pygame.event.get()  # 获取事件列表
    # if len(event_list) > 0:
    #     print(event_list)
    for event in event_list:
        if event.type == pygame.QUIT:  # 关闭按钮事件
            print('退出游戏...')
            pygame.quit()
            exit()

    hero_rect.y -= 2              # 移动效果的实现
    if -hero_rect.height > hero_rect.y:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))  # 注意其他绘制要在背景后，不然会被背景覆盖
    screen.blit(hero, hero_rect)   # 利用背景覆盖原来的游戏元素
    enemy_group.update()  # 更新精灵位置
    enemy_group.draw(screen)  # 在屏幕上绘制精灵图像
    pygame.display.update()

