"""
Solution for fourth task of second homework
"""

import sys
from builtins import print
from collections import defaultdict
from queue import Queue


class Graph:
    """Graph implementation with BFS and DFS function"""
    def __init__(self, edges):
        self._graph = defaultdict(list)
        for edge in edges:
            assert len(edge) == 2
            self._graph[edge[0]].append(edge[1])
            self._graph[edge[1]].append(edge[0])

    def bfs(self, start_vertex=0):
        """
        visit graphs vertexes with bfs algorithm
        :param start_vertex
        :return: void
        """
        assert start_vertex in self._graph, "start vertex not in graph"
        passed = defaultdict(bool)
        passed[start_vertex] = True
        queue = Queue()
        queue.put(start_vertex)

        while not queue.empty():
            curr = queue.get()
            print(curr)
            for vertex in self._graph[curr]:
                if not passed[vertex]:
                    queue.put(vertex)
                    passed[vertex] = True

    def dfs(self, start_vertex=0):
        """
        visit graphs vertexes with dfs algorithm
        non recursive version of dfs algorithm described here
        https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%83
        :param start_vertex
        :return: void
        """
        assert start_vertex in self._graph, "start vertex not in graph"
        passed = defaultdict(bool)
        stack = [[start_vertex, None]]
        print(start_vertex)
        passed[start_vertex] = True
        current_index = defaultdict(lambda: -1)

        while stack:
            cur = stack[-1]
            current_index[cur[0]] += 1
            if len(self._graph[cur[0]]) > current_index[cur[0]]:
                cur[1] = self._graph[cur[0]][current_index[cur[0]]]
                if not passed[cur[1]]:
                    passed[cur[1]] = True
                    print(cur[1])
                    stack.append([cur[1], None])
            else:
                stack.pop()


def main():
    """Just a main function"""
    lst = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    graph = Graph(lst)
    print("BFS:")
    graph.bfs()
    print("\nDFS:")
    graph.dfs()

    lst = [[0, 3], [1, 3], [2, 3], [4, 3], [2, 5]]
    graph = Graph(lst)
    print("\nBFS:")
    graph.bfs()
    print("\nDFS:")
    graph.dfs()
    return 0


if __name__ == '__main__':
    sys.exit(main())
