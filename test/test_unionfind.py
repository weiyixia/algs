import unittest
import random
import timeout_decorator
from algs.unionfind import UnionFind
class TestUnionFind(unittest.TestCase):
    def test_1(self):
        uf = UnionFind(10)
        self.assertEqual(uf.find(0), 0)

    def test_2(self):
        uf = UnionFind(10)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)
        uf.union(3, 4)
        self.assertEqual(uf.connected(0,4), True)

    @timeout_decorator.timeout(100)
    def test_3(self):
        uf = UnionFind(100000)
        for i in range(500000):
            p = random.randint(0, 9999)
            q = random.randint(0, 9999)
            uf.union(p, q)

