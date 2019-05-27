# 元组tuple 元素不能修改

# 取值，统计 .count() .index()

# 应用 1.函数参数，返回值  2.格式化字符串 3.tuple()防止list被修改

a = [1, 2, 3, 4]
a = tuple(a)

print(a)


# 字典 dict()  {} 无序 键值对  key唯一

# 取值 dict[key] .get()

# 增加/修改  dict[key]

# 删除 .pop() .clear()

# .values() .keys() .items()

# 合并 .update()

b = {'1': 'a', '2': 'b'}

print(isinstance(b.items(), object))
for k, v in b.items():
    print(k, v)


b.pop('2')
b.update({'3': 1})

for k in b:
    print(k, b[k])

# 应用：描述复杂的数据信息，
# 将多个字典放入列表中再遍历