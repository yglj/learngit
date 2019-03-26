def trim(s):
    while s != '' and (s[0] == ' ' or s[-1] == ' '):
        if s[-1] ==' ':
            s = s[:-1]  
        elif s[0] == ' ':
            s = s[1:]
    return s

'''
def trim(s):
    if s == "":
        return s
    if s[len(s)-1] ==" ":
        i = len(s)-1
        while i:
            if s[i] != " ":
                s = s[:i+1]
                break
            i-=1
    if s[0] == ' ':
        for i in range(len(s)):
            if s[i] != ' ':
                s = s[i:]
                break
            elif i == len(s)-1:
                return ''
    return s
'''
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')  
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
