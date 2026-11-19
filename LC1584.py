class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)

        # we compose every possible edge weighted by Manhattan distance
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                edges.append((abs(xi - xj) + abs(yi - yj), i, j))

        # We then sort edges from cheapest to most expensive
        edges.sort()

        # Then we can use Union-Find to detect cycles
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False         
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra                
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        # Then we take the cheapest edge that doesn't form a cycle
        total, used = 0, 0
        for cost, i, j in edges:
            if union(i, j):
                total += cost
                used += 1
                if used == n - 1:
                    break
        return total
