"""
Solution for sixth task of second homework
"""

import sys
from builtins import print
from collections import defaultdict


class Graph:
    """Graph implementation with find signal spread time function"""
    def __init__(self, edges):

        self._graph = defaultdict(list)
        length = 0
        weight = 0
        for edge in edges:
            assert len(edge) == 3
            weight = max(edge[2], weight)
            length = max(edge[0], edge[1], length)

            self._graph[edge[0]].append((edge[2], edge[1]))
            self._graph[edge[1]].append((edge[2], edge[0]))

        self.len = length + 1
        self.inf = self.len * weight + 1

    def find_shortest_way(self, start_node, end_node):
        """https://e-maxx.ru/algo/dijkstra"""
        assert 0 <= start_node <= self.len
        assert 0 <= end_node <= self.len

        cur_node = start_node

        dist = [(self.inf, i) for i in range(self.len)]
        dist[cur_node] = (0, cur_node)
        remaining = set(dist)

        while remaining:
            node_cur_st = min(remaining)
            cur_dist, cur_node = node_cur_st
            remaining.remove(node_cur_st)

            if cur_dist == self.inf:
                continue

            for sub_dist, sub_node in self._graph[cur_node]:
                if sub_dist + cur_dist < dist[sub_node][0]:
                    remaining.remove(dist[sub_node])
                    dist[sub_node] = (sub_dist + cur_dist, sub_node)
                    remaining.add(dist[sub_node])

        if dist[end_node][0] == self.inf:
            return -1
        return dist[end_node][0]


def main():
    """Just a main function"""
    dists = [[0, 3, 5], [1, 3, 11], [2, 3, 56], [4, 3, 77], [5, 4, 89]]
    assert Graph(dists).find_shortest_way(0, 1) == 16
    assert Graph(dists).find_shortest_way(1, 2) == 67
    assert Graph(dists).find_shortest_way(3, 2) == 56
    assert Graph(dists).find_shortest_way(4, 2) == 133
    assert Graph(dists).find_shortest_way(5, 1) == 177
    print("tests ok")

    lst = eval(input("Provide a list: "))
    start_node = int(input("Provide a start_node id: "))
    end_node = int(input("Provide an end_node id: "))
    print(Graph(lst).find_shortest_way(start_node, end_node))


if __name__ == '__main__':
    sys.exit(main())
