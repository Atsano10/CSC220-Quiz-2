class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)

        # we compose every possible edge weighted by Manhattan distance (Pair up points with other points) 
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                edges.append((abs(xi - xj) + abs(yi - yj), i, j))

        # We then sort edges, .sort() by default sorts in an increasing order.
        edges.sort()

        # Then we can use Union-Find to detect cycles
        parent = list(range(n)) # everyone starts out as its own "team" and then connect afterwards.
        rank = [0] * n

        def find(x): #checks who the "leader" of a point or if its connected to something. 
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb: # means the points are already connected so it just proceeds
                return False         
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra # not connected so it connects them.         
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        # Whenever we join points its cost is added to the total, and we stop once we have n-1 cables. 
        total, used = 0, 0
        for cost, i, j in edges:
            if union(i, j):
                total += cost
                used += 1
                if used == n - 1:
                    break
        return total

# For presentation purposes: We list every possible connection, sort them by cost, and greedily take the cheapest one that doesn’t create a cycle. 
# Union-Find tells us whether two points are already connected. Once we have n − 1 connections, everything is linked at the minimum cost.

