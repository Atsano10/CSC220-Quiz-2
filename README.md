<h1 align="center">QUIZ 2: GRAPH ALGORITHMS SPRINT</h1>

<p align="center">
  <b>LeetCode Interview Prep</b><br>
  <b>CSC 22000-P: Algorithms</b> • Fall 2026
</p>
<p align="center">
  <b>Contributors:</b> Apostolos Tsano, Junyu Chen, Haoyang Liang
</p>

---

## Part 1: Solve BOTH Problems

**Time Limit:** 45 minutes

**Format:** You must work in groups of 3–4. Working alone is not permitted.

**Instructions:** Choose any programming language you like. Log in to LeetCode, write your solutions for **BOTH** problems below, and ensure they pass all test cases.

### Problem 1: Min Cost to Connect All Points (LeetCode #1584)

**Algorithm Focus:** Minimum Spanning Tree (Kruskal’s Algorithm)

**Problem Statement:** You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`. The cost of connecting two points is the Manhattan distance between them. Return the minimum cost to make all points connected.

**Link:** https://leetcode.com/problems/min-cost-to-connect-all-points/

- **Time Complexity:** O(n^2 log n^2)
- **Space Complexity:** O(n^2)

### Problem 2: Find the City With the Smallest Number of Neighbors at a Threshold Distance (LeetCode #1334)

**Algorithm Focus:** All-Pairs Shortest Path (Floyd-Warshall Algorithm)

**Problem Statement:** There are `n` cities numbered from `0` to `n − 1`. Given the array `edges` where `edges[i] = [from, to, weight]` represents a bidirectional and weighted edge, and an integer `distanceThreshold`. Return the city with the smallest number of cities that are reachable through some path and whose distance is at most `distanceThreshold`. If there are multiple such cities, return the city with the greatest number.

**Link:** https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighborsat-a-threshold-distance/

- **Time Complexity:** O(n^3)
- **Space Complexity:** O(n^2)

---

## Part 2: Demo Time & Grading

- At the end of the time limit, one person from your group will present for the entire group.

**Presentation Format (2 Minutes Maximum):**

1. **Algorithms:** Tell the class which graph algorithm you used for each of the two problems.
2. **Explain the code:** Briefly walk through your logic for ONE of the problems.
3. **Live Demo:** Click “Submit” on LeetCode in front of me to prove your code compiles, runs, and passes all test cases.

**Grading Rubric:**

- **50%:** Live Demo (Code officially passes all LeetCode test cases).
- **40%:** Explanation (Clearly explaining the graph algorithm used).
- **10%:** GitHub link submitted to Brightspace with a README.

* Used AI for formatting the readme using markdown and simple html code.
