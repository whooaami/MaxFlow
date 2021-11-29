import unittest
from main import FordFulkerson


class TestMain(unittest.TestCase):

    def test_ford(self):
        graph = [[0, 16, 13, 0, 0, 0],
                 [0, 0, 10, 12, 0, 0],
                 [0, 4, 0, 0, 14, 0],
                 [0, 0, 9, 0, 0, 20],
                 [0, 0, 0, 7, 0, 4],
                 [0, 0, 0, 0, 0, 0]]
        g = FordFulkerson(graph)

        expected = 23
        self.assertEqual(g.ford_fulkerson(source=0, sink=5), expected)
