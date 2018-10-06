# ascii编码  一个字节
# python3 默认个utf-8
# utf-8 是unicode编码的一种编码格式  # 汉字使用3个字节


hello = u'hi 世界'
# print(hello)
for i in hello:
    print(i)

# eval（） 将字符串当成有效表达式，并返回结果

eval('print(hello)')

# input_str = input('输入计算表达式：')
# print('结果等于：%s' % eval(input_str))

# 谨慎使用eval()
eval("__import__('os').system('ls')") # 导入os模块，调用系统命令，并执行终端命令
