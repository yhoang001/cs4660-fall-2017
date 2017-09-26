"""test_search tests the search implementation in simple graph"""

import unittest

from search import searches
from graph import graph

class TestBFS(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_graph(graph_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_graph(graph_2_path), self.graph_1s))

    def test_bfs_1(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1),
                    graph.Edge(graph.Node(10), graph.Node(8), 1)
                ],
                searches.bfs(g, graph.Node(1), graph.Node(8))
            )

    def test_bfs_2(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1)
                ],
                searches.bfs(g, graph.Node(1), graph.Node(10))
            )

    def test_bfs_3(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ],
                searches.bfs(g, graph.Node(1), graph.Node(5))
            )

    def test_bfs_4(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(5), 11)
                ],
                searches.bfs(g, graph.Node(0), graph.Node(5))
            )

    def test_bfs_5(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7)
                ],
                searches.bfs(g, graph.Node(0), graph.Node(2))
            )

class TestDFS(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_graph(graph_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_graph(graph_2_path), self.graph_1s))

    def test_dfs_1(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1),
                    graph.Edge(graph.Node(5), graph.Node(0), 1),
                    graph.Edge(graph.Node(0), graph.Node(7), 1),
                    graph.Edge(graph.Node(7), graph.Node(8), 1)
                ],
                searches.dfs(g, graph.Node(1), graph.Node(8))
            )

    def test_dfs_2(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1),
                    graph.Edge(graph.Node(5), graph.Node(0), 1),
                    graph.Edge(graph.Node(0), graph.Node(7), 1),
                    graph.Edge(graph.Node(7), graph.Node(10), 1)
                ],
                searches.dfs(g, graph.Node(1), graph.Node(10))
            )

    def test_dfs_3(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ],
                searches.dfs(g, graph.Node(1), graph.Node(5))
            )

    def test_dfs_4(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7),
                    graph.Edge(graph.Node(2), graph.Node(5), 2)
                ],
                searches.dfs(g, graph.Node(0), graph.Node(5))
            )

    def test_dfs_5(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7)
                ],
                searches.dfs(g, graph.Node(0), graph.Node(2))
            )

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        graph_1_path = './test/fixtures/graph-1.txt'
        graph_2_path = './test/fixtures/graph-2.txt'
        self.graph_1s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_2s = [graph.AdjacencyList(), graph.AdjacencyMatrix(), graph.ObjectOriented()]
        self.graph_1s = list(map(construct_graph(graph_1_path), self.graph_1s))
        self.graph_2s = list(map(construct_graph(graph_2_path), self.graph_1s))

    def test_dijkstra_1(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1),
                    graph.Edge(graph.Node(10), graph.Node(8), 1)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(8))
            )

    def test_dijkstra_2(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(10))
            )

    def test_dijkstra_3(self):
        for g in self.graph_1s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(5))
            )

    def test_dijkstra_4(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(1), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 5)
                ],
                searches.dijkstra_search(g, graph.Node(1), graph.Node(5))
            )

    def test_dijkstra_5(self):
        for g in self.graph_2s:
            self.assertEqual(
                [
                    graph.Edge(graph.Node(0), graph.Node(6), 3),
                    graph.Edge(graph.Node(6), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 5)
                ],
                searches.dijkstra_search(g, graph.Node(0), graph.Node(5))
            )

def construct_graph(graph_path):
    """Helper function to construct graph given graph_path"""
    return lambda g: graph.construct_graph_from_file(g, graph_path)
