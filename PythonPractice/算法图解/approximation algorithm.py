"""
不可能完成的任务，没有快速算法的问题，NP完全问题
识别NP完全问题，近似算法，学习贪婪策略
旅行商问题和集合覆盖问题共同之处：从中选出最小/最短的那个
"""
state_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}  # 未覆盖的州
stations = {'one': {'id', 'nv', 'ut'}, 'two': {'wa', 'id', 'mt'}, 'three': {'or', 'nv', 'ca'}, 'four': {'nv', 'ut'},
            'five': {'ca', 'az'}}

final_stations = set()

# print(type(state_needed))
while state_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = state_needed & states_for_station  # 交集
        if len(covered) > len(states_covered):
            states_covered = covered
            best_station = station
    state_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)