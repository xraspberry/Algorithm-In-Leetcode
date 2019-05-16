"""

Dijkstra 最短路径算法
每次选择出来的都是离开始节点最短的路径
时间复杂度O(ElogE)
空间复杂度O(E)
"""
from queue import PriorityQueue


def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    cands = PriorityQueue([(0, v0, v0)])
    while count < vnum and not cands.empty():
        # 优先级队列保证了选择出来的是目前离v0最短的节点
        # 所以可以保证，每次取出来就可以确定一个节点的最短路径
        plen, u, vmin = cands.get()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.put((plen+w, vmin, v))
        count += 1
    return paths
