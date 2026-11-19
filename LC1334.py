
class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        
        # A really big number for comparisons.
        INF = float('inf')

        # We then make a matrix filled with inifinity in each index. (A square matrix.)
        dist = [[INF] * n for _ in range(n)]

        # We then go through every city and set the distance to it's self as 0.
        for i in range(n):
            dist[i][i] = 0

        # Go through each road.
        for u, v, w in edges:
            # Store u-v, and keep the min if a shorter one was already stored.
            dist[u][v] = min(dist[u][v], w)
            # check the road in the opposite direction.
            dist[v][u] = min(dist[v][u], w)

        # this is the algorithm : Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # keep whichever is the shorter distance:
                    dist[i][j] = min(
                        # we calculate the best route from i to j 
                        dist[i][j],
                        # we go from i to k first and then k to j 
                        dist[i][k] + dist[k][j]
                    )

        # placeholder
        answer = -1

        # this is the fewest reachable cities so far.
        min_count = n

        # then we check each city as a possible destination
        for i in range(n):
            count = 0

            for j in range(n):
                # skip the city itself and then loop and count the cities whose distance is within the 
                # threshold. Cities that can not be reached are counted as INF.
                if i != j and dist[i][j] <= distanceThreshold:
                    # this is for the reachable cities.
                    count += 1

            # this is for the city that reaches the fewest or ties the best city so far.  
            if count <= min_count:
                min_count = count
                answer = i

        # return the fewest reachable neighbors.
        return answer

# Complexity:
#
# Time complexity is O(n^3) becayse we have three nested loops.
#  
# Space complexity is O(n^2) because the largest thing stored is our square matrix.
# 

