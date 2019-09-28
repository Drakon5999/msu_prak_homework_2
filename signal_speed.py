"""
Solution for sixth task of second homework
"""

import sys
from builtins import print

MAX_N = 100
MAX_W = 100


class Graph:
    """Graph implementation with find signal spread time function"""
    def __init__(self, edges, n):
        self._graph = [[] for _ in range(n)]
        for edge in edges:
            assert len(edge) == 3
            assert 0 < edge[0] <= n
            assert 0 < edge[1] <= n
            assert 0 <= edge[2] < MAX_W

            self._graph[edge[0]-1].append((edge[2], edge[1]-1))
            self._graph[edge[1]-1].append((edge[2], edge[0]-1))

    def find_signal_spread_time(self, start_node):
        """https://e-maxx.ru/algo/dijkstra"""
        length = len(self._graph)
        assert 0 < start_node <= length

        cur_node = start_node - 1
        inf = MAX_N * MAX_W + 1

        dist = [(inf, i) for i in range(length)]
        dist[cur_node] = (0, cur_node)
        remaining = set(dist)

        while remaining:
            node_cur_st = min(remaining)
            cur_dist, cur_node = node_cur_st
            remaining.remove(node_cur_st)

            if cur_dist == inf:
                return -1

            for sub_dist, sub_node in self._graph[cur_node]:
                if sub_dist + cur_dist < dist[sub_node][0]:
                    remaining.remove(dist[sub_node])
                    dist[sub_node] = (sub_dist + cur_dist, sub_node)
                    remaining.add(dist[sub_node])

        return max(dist)[0]


def main():
    """Just a main function"""
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    X = 2
    assert Graph(times, N).find_signal_spread_time(X) == 2
    print("test ok")


if __name__ == '__main__':
    sys.exit(main())
