"""
Kruskal -> 抽象算法，算法模式

空间复杂度是O(max(e, v))，因为连通图中，总有O(e)>=O(v)
所以总的空间复杂度是O(e)

贪心算法，对于最小生成树问题来说，可以证明某些贪心策略的确可以获得具有最小权值的生成树
"""


def kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    # 排序时间复杂度为O(eloge)
    edges.sort()
    # 这里时间复杂度是O(e), 内部条件判断与小循环时间复杂度是O(v2)
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi, vj, w))
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    # 所以总的时间复杂度是O(max(eloge, v2))
    return mst