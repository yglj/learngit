
import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # 使用常量定义游戏窗口大小
FRAME_PER_SEC = 60  # 刷新帧率
CREATE_ENEMY_EVENT = pygame.USEREVENT  # 创建敌机定时器常量
CREATE_BULLET_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """
    游戏精灵类： 初始化通用属性
    """

    def __init__(self, image_name, speed=1):
        super().__init__()  # 调用父类初始化方法
        self.image = pygame.image.load(image_name)  # 图像
        self.rect = self.image.get_rect()  # 区域大小
        self.speed = speed  # 运动速度

    def update(self):
        """
        位置跟新
        :return:
        """
        self.rect.y += self.speed
        # print(self.rect)


class BackGround(GameSprite):
    """
    背景类需求： 重写游戏精灵类方法，实现背景的交替滚动
    """
    def __init__(self, first=True):
        super().__init__('images/background.png')
        if not first:
            self.rect.y = -self.rect.height

    def update(self):
        """
        更新位置，如果背景图像移出屏幕，将其设置到屏幕上方
        :return:
        """
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """
    敌机类需求:
    使用定时器set_timer()创建敌机， 第一个参数是事件代号，第二个参数是触发间隔
    """
    def __init__(self):
        # GameSprite.__init__(self, 'images/enemy1.png')
        super().__init__('images/enemy1.png')
        self.speed = (random.random() + 0.2) * 3   # 初始随机速度
        self.rect.bottom = 0   # 初始位置坐标
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        """
        敌机位置更新
        :return:
        """
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print('敌机飞出屏幕，从精灵组中删除')
            self.kill()

    def __del__(self):
        print('敌机挂了%s' % self.rect)


class Hero(GameSprite):
    """
    英雄机：
    1.由键盘控制移动，移动范围不能超出屏幕
    2.可以上下左右按键移动
    3.0.5秒发射一次子弹，一次发射三枚子弹，子弹碰到敌机，敌机销毁
    4.碰到敌机销毁
    """
    def __init__(self):
        super().__init__('images/me1.png')
        self.rect.x = 200
        self.rect.y = 500
        self.speed = 0
        # self.bullet_group = pygame.sprite.Group()

    def update(self, x=0, y=0):
        """
        英雄机移动控制
        :return:
        """
        self.rect.x, self.rect.y = pygame.mouse.get_pos()
        self.rect.x -= self.rect.width // 2
        self.rect.y -= self.rect.height // 2
        # self.rect.x += x
        # self.rect.y += y

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
        # print('英雄机：', self.rect)


class Bullet(GameSprite):
    """
    子弹类
    """
    def __init__(self, x, y):
        super().__init__('images/bullet1.png')
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """

        :return:
        """
        self.speed = 5
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

    def __del__(self):
        print('子弹消失')
