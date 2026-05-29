# 8-Puzzle-

This project is very interesting as it shows how can a good heuristic function can improve the performance of the whole algorithm. In this project 
I have implemented a search algorithm with and without Heuristics. An Heuristic function is used in Search, and it finds the most promising path. 
It takes the current state of the agent as its input and produces the estimation of how close agent is from the goal. The search algorithm used 
here is a Uniform cost search algorithm that uses the lowest cumulative cost to find a path from the source to the destination.
I have also implemented it using two different heuristics one being A* with Misplaced Tile Heuristic and the other A* with ManhattanDistance Heuristic. 
There were puzzles of varying difficulty given to implement. The easiest one being the goal state itself and the hardest one being impossible to solve.
However for the goal state all the algorithms performed similar, There is was an interesting observation has the difficulty level increased. 
The observation showed that for higher difficulties uniform cost search without heuristic was not a good choice as the number of nodes expanded was the highest.
Among the heuristic algorithms A* with Manhattan distance heuristic algorithm expands less nodes when increasing the depth of the tree as it  approximates which
nodes to explore next better than the A* with Misplaced tile heuristic.

