# encoding=utf-8
"""
封装主游戏类，创建游戏对象，启动游戏
一，游戏初始化：设置游戏窗口，创建游戏时钟，创建精灵，精灵组
二，游戏循环:设置刷新帧率，事件监听，碰撞检测，更新绘制精灵组，跟新屏幕显示

"""

from hm_pygame.plane_sprites import *


class PlaneGame:
    """
    飞机主游戏类
    """
    def __init__(self):
        print('初始化游戏...')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        self.enemy_timer = pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 设置每秒执行一次的定时器事件
        self.bullet_timer = pygame.time.set_timer(CREATE_BULLET_EVENT, 500)

    def __create_sprites(self):
        self.bg1 = BackGround()
        self.bg2 = BackGround(False)
        self.bg_group = pygame.sprite.Group(self.bg1, self.bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.bullet_group = pygame.sprite.Group()

    def __event_handler(self):
        """
        事件监听
        :return:
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)

            if event.type == CREATE_BULLET_EVENT:
                bullets = []
                for i in range(1, 4):
                    bullet = Bullet(self.hero.rect.centerx, self.hero.rect.y - (i * 20))
                    print('biu')
                    bullets.append(bullet)
                self.bullet_group.add(bullets)

        pressed = pygame.key.get_pressed()  # 获取按键元组
        if pressed[pygame.K_LEFT]:
            self.hero.update(x=-2)
        elif pressed[pygame.K_RIGHT]:
            self.hero.update(x=2)
        elif pressed[pygame.K_UP]:
            self.hero.update(y=-2)
        elif pressed[pygame.K_DOWN]:
            self.hero.update(y=2)

    def __update(self):
        """
        精灵组位置更新
        :return:
        """
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.bullet_group.update()
        self.bullet_group.draw(self.screen)
        pygame.display.update()

    def __check_collide(self):
        if pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, True, True):
            print('敌机被消灭')
        if pygame.sprite.groupcollide(self.enemy_group, self.hero_group, True, None):
            self.hero.kill()
            self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        print('游戏结束！')
        exit()

    def start_game(self):
        """
        开始循环游戏游戏
        """
        print('开始游戏...')
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__update()
            self.__check_collide()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
