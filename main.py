
import time

class NaiveUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def test_naive_union_find(n):
    uf = UnionFind(n)
    start_time = time.time()
    for i in range(n):
        uf.union(i, i + 1)
    end_time = time.time()
    print(f"[NaiveUnionFind] Time taken for {n} operations: {end_time - start_time} seconds")

test_naive_union_find(10000)

def test_union_find(n):
    uf = UnionFind(n)
    start_time = time.time()
    for i in range(n):
        uf.union(i, i + 1)
    end_time = time.time()
    print(f"[UnionFind] Time taken for {n} operations: {end_time - start_time} seconds")

test_union_find(10000)
