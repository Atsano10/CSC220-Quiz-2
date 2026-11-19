
class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        # Step 1: Initialize distance matrix
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        # Step 2: Add undirected edges
        for u, v, w in edges:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)

        # Step 3: Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

        # Step 4: Find the city with fewest reachable neighbors
        answer = -1
        min_count = n

        for i in range(n):
            count = 0

            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                answer = i

        return answer

