class UnionFind:
    
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
            
    def union(self, x, y):
        rootX = self.find(x)    
        rootY = self.find(y)
        
        if rootX == rootY:
            return False
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
                
        self.count -= 1
        return True
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)            
        for pair in edges:
            if not unionFind.union(*pair):
                return False
        return unionFind.count == 1
    