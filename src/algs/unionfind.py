"""
The UnionFind class implements the union-find data structure.
The union-find data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
It provides near-constant-time operations to add new sets, to merge existing sets, and to determine whether elements are in the same set.
"""
import array as arr
class UnionFind:
    def __init__(self, n):
        self.n = n
        #parent[i] = parent of i
        self.parent = arr.array('i', range(n))
        # rank[i] = rank of subtree rooted at i
        self.rank = arr.array('i', [0] * n)

    def find(self, p):
        #the path compression algorithm
        # Follow links to find a root.
        root = p
        while root != self.parent[root]:
            root = self.parent[root]
        while p != root:
            #first get the parent of p, then change p's parent to root
            newp = self.parent[p]
            self.parent[p] = root
            p = newp
        return root

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.rank[rootp] < self.rank[rootq]:
            self.parent[rootp] = rootq
        elif self.rank[rootp] > self.rank[rootq]:
            self.parent[rootq] = rootp
        else:
            self.parent[rootq] = rootp
            self.rank[rootp] += self.rank[rootq]

    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq
