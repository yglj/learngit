# 封装 对象的细节封装到类的内部，让对象调用
import random


class Man:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print('%s 太胖了，他决定减肥了' % self.name)

    def run(self):
        self.weight -= 0.5
        print('%s 跑步减少了0.5kg' % self.name)

    def eat(self):
        self.weight += 1
        print('%s 控制不住几级，体重增加1kg' % self.name)

    def __str__(self):
        return '%s 现在体重为 %s kg' % (self.name, self.weight)


# x = Man('xiaoming', 75)
# for i in range(10):
#     choice = random.randint(0,2)
#     if choice:
#         x.run()
#     else:
#         x.eat()
#
# print(x)


class HouseItem:  # 家具类

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '%s占地%s平米' % self.name, self.area


desk = HouseItem('梳妆台', 1.5)
board = HouseItem('衣柜', 2.5)
bed = HouseItem('席梦思', 4)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.house_items = []

    def add_items(self, item):
        if self.area < item.area:
            print('%s面积太大无法放置' % item.name)
            return
        self.house_items.append(item.name)
        self.area = self.area - item.area
        print('剩余%s平米' % self.area)

    def __str__(self):
        return '户型【%s】\t面积【%s】\t家具【%s】' \
               % (self.house_type,
                  self.area,
                 self.house_items)


house = House('小户型', 75)
house.add_items(desk)
house.add_items(bed)
house.add_items(board)
print(house)