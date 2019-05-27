"""
散列表（哈希）
散列函数：将不同的输入映射到不同的索引， 用散列函数来确定内存地址
作用：查找，防止重复，用作缓存
冲突：通过函数得到同样的哈希值， 数组+链表
性能：平均O(1) 常量时间， 最糟O(n)
较低的填装因子（不大于0.7），良好的散列函数
"""

# 检查投票
voted = {}
def check_voter(name):
    if voted.get(name):
        return "kick them out!"
    else:
        voted[name] = True
        print('let them vote!')


# 缓存网页
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = 'gt_data_from_server(url)'
        cache[url] = data
        return data