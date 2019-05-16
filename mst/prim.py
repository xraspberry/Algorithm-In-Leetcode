"""

时间复杂度为O(eloge)
空间复杂度为O(e)，因为对于连通图来说 O(e)>=O(v)
"""

from queue import PriorityQueue


def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    # 优先级队列出队入队的时间O(logn)
    # 所以e条边，则时间复杂度为O(eloge)
    cands = PriorityQueue([(0, 0, 0)])
    count = 0
    while count < vnum and not cands.empty():
        w, u, v = cands.get()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.put((w, v, vi))
    return mst
