
# 查看全局变量
# g = globals()
# for k,v in g['__builtins__'].__dict__.items():
#     print(k, '==>', v)


# 动态创建类

# def choice_class(name):
#     if name == 'a':
#         class A:
#             pass
#         return A()
#     elif name == 'b':
#         class B:
#             pass
#         return B()
#
#
# a = choice_class('a')
# print(hasattr(a, 'field_one'))
# setattr(a, 'field_one', 1)
# print(a.field_one)

# 使用type创建类

@staticmethod
def call_a():
    print('this is staticmethod')


@classmethod
def call_b(cls):
    print('this is class method')


def call_c(self):
    print('this is instance method')


TypeCreateClass = type('TypeCreateClass', (object, ), {'a': '这是类属性',
                                                       'call_a': call_a,
                                                       'call_b': call_b,
                                                       'call_c': call_c})
test1 = TypeCreateClass()
print(test1.a)
test1.call_a()
test1.call_b()
test1.call_c()
help(TypeCreateClass)
print(TypeCreateClass.__class__.__class__)


# 元类

class MetaClassCreator(type):
    def __new__(cls, name, bases, attrs):  # 创建对象的特殊方法
        # 有两个类方法时，第二个遍历时会跳过
        for k, v in attrs.items():
            print(attrs.items())
            if not k.startswith('__') and k.islower():
                attrs[k.upper()] = v
                attrs.pop(k)  # 问题出在这里，先删后添 dictionary changed size during iteration
        return type.__new__(cls, name, bases, attrs)
        # new_attr = {}
        # for name, value in attrs.items():
        #     if not name.startswith("__"):
        #         new_attr[name.upper()] = value
        #     else:
        #         new_attr[name] = value
        # return type.__new__(cls, name, bases, new_attr)


class TestClass(object, metaclass=MetaClassCreator):
    one = 111
    two = 222
    there = 333
    # four = 444
    # five = 555

    def __init__(self, a, b):
        self.a = a
        self.b = b


test2 = TestClass('a', 'b')
print(dir(test2))
assert not hasattr(test2, 'TWO'), 'has attrs TWO'










