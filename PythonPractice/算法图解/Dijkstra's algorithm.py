"""
狄克斯特拉算法
每条边上的关联数字称为权重
带权重的图叫加权图
寻找加权图的最短路径
只是用于有向无环图
"""

graph = {}  # 加权图
costs = {}  # 开销
parents = {}  # 父节点

# 图的各顶点的邻居及边的权重
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# print(graph['start'].keys())
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')  # 无穷大
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None  # 开始没有到达fin的路径

processed = []

"""
1.只要还有要处理的节点
2.获取离起点最近的节点
3.更新其邻居的开销
4.如果有邻居的开销被更新，同时更新其父节点
5.将该节点标记为处理过
"""


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


if __name__ == '__main__':
    main()
    # print(parents)
    # print(costs)
    # print(graph)
    processed.insert(0, 'start')
    path = '->'.join(processed)
    print(path)
