# algorithms-for-8-puzzle
implemented several search algorithms to solve the 8-puzzle problem with Python:
DFS, BFS, IDS, Greedy Best-First (hence-forth "Greedy"), A*, IDA*.

• Search methods to be implemented (use the exact function interface ): dfs, bfs, ids, greedy, a-star, ida-star.
need to change the name of the searching function, like bfs,a_star, in the main() function.

• Test and compare time and space complexity for all cases.
• Test and compare the effect of different heuristic functions (for the informed search algorithms).
   • Use h1 (number of tiles out-of-place), and h2 (sum of manhattan distance)  

Input: a board configuration
      ’(1 3 4 8 6 2 7 0 5)
Output: sequence of moves
      ’(UP RIGHT UP LEFT DOWN)
 
For example, using BFS, result is like this:
 -------------
| 1 | 3 | 4 |
-------------
| 8 | 0 | 2 |
-------------
| 7 | 6 | 5 |
-------------
-------------
| 1 | 3 | 4 |
-------------
| 8 | 2 | 0 |
-------------
| 7 | 6 | 5 |
-------------
-------------
| 1 | 3 | 0 |
-------------
| 8 | 2 | 4 |
-------------
| 7 | 6 | 5 |
-------------
-------------
| 1 | 0 | 3 |
-------------
| 8 | 2 | 4 |
-------------
| 7 | 6 | 5 |
-------------
-------------
| 1 | 2 | 3 |
-------------
| 8 | 0 | 4 |
-------------
| 7 | 6 | 5 |
-------------
['up', 'right', 'up', 'left', 'down']
5  moves
Total searching time: 0.00130 seconds

BFS can return the optimal solution, because it always
expands the shallowest unexpected node. However, it saves every node it searches ,so the space it
takes is very large, which is its major problem. When the input is hard, it gets more difficult for BFS
to obtain the result.
