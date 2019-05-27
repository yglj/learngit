from django.template import Library
# 自定义过滤器函数，最多两个参数
register = Library()


@register.filter
def mod(num):
    # 判断num是否是偶数
    return num % 2 == 0


@register.filter
def mods(num, value):
    # 判断num是否能被value整除
    return num % value == 0
