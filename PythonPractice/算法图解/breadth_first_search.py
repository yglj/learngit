"""
1.图：有节点（node）和边（edge）组成的一组连接，有向图，无向图 O（V+E）
2.广度优先搜索（BFS）:能找出两样东西之间的最短距离 ,
3.最短路径问题（shortest-path-problem）：使用图建模，再使用广度优先搜索
4.队列（queue） 一种先进先出数据结构（FIFO）
4.树是一种特殊的图， 没有往后指的边
"""


from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def search(name):
    searched = []
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        people = search_queue.popleft()
        if people not in searched:
            if person_is_seller(people):
                print('%s is mango seller' % people)
                return True
            else:
                searched.append(name)
                search_queue += graph[people]
    return False


def person_is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    print(search('you'))