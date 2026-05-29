import puzzle_solver_2 as ps2
import time

class Puzzle:
    def __init__(self,size):
        self.n = size
        self.start_node = []
        self.end_node = []
        self.nodeexpanded = 0
    
    def depth_cost(self,child_object,goal): # calculating f(n)
            return self.heuristic(child_object.puzzle,goal)+child_object.depth
    
    def heuristic(self,starting_puzzle,goal): # calculating h(n)
            temp = 0
            for i in range(0,self.n):
                for j in range(0,self.n):
                    if starting_puzzle[i][j] != goal[i][j] and starting_puzzle[i][j] != '0':
                        temp += 1
            return temp
    
    def manhattan_distance_heuristic(self, starting_puzzle): # calculate h(n) for Manhattan 
        puzzle = []
        for x in starting_puzzle:
            for y in x:
                puzzle.append(int(y))
        h=0
        for index, value in enumerate(puzzle):
            if value !=0:
                a = abs((value-1)%3 - index%3)
                b = abs((value-1)//3 - index//3)
                h+= a + b
        return h
    
    def process(self, puzzle, algo):
            start_time = time.time()
            starting_puzzle = puzzle
            depth_changed = []
            nodes = []
            time_taken = []
            goal = [['1','2','3'],['4','5','6'],['7','8','0']]
            child_object = ps2.Child(starting_puzzle,0,0)
            if algo == 1:
                child_object.low_cost_depth = child_object.depth
            elif algo == 2:
                child_object.low_cost_depth = self.depth_cost(child_object, goal)
            else:
                child_object.low_cost_depth = self.manhattan_distance_heuristic(child_object.puzzle) + child_object.depth
            self.start_node.append(child_object)
            while True:
                current_state_object = self.start_node[0]
                if algo != 1:
                    print('\ng(n): {0}, h(n): {1}'.format(current_state_object.depth,self.heuristic(current_state_object.puzzle,goal)))
                else:
                    print('\ng(n): {0}, h(n): {1}'.format(current_state_object.depth,0))
                for row in current_state_object.puzzle:
                    for value in row:
                        print(value,end=" ")
                    print("")
                if current_state_object.depth not in depth_changed:
                    depth_changed.append(current_state_object.depth)
                    nodes.append(self.nodeexpanded)
                    time_taken.append(time.time())
                if(self.heuristic(current_state_object.puzzle,goal) == 0):
                    end_time = time.time()
                    print('\nGoal state reached')
                    print('\nNode extended: {0}'.format(self.nodeexpanded))
                    print('\nDepth reached: {0}\n'.format(current_state_object.depth))
                    print('\nTime_taken: {:.2f} seconds'.format(end_time-start_time))
                    break
                for current_node in current_state_object.node_expand():
                    if algo == 2:
                        current_node.low_cost_depth = self.depth_cost(current_node,goal)
                    elif algo == 1:
                        current_node.low_cost_depth = current_node.depth
                    else:
                        current_node.low_cost_depth = self.manhattan_distance_heuristic(current_node.puzzle) + current_node.depth
                    self.start_node.append(current_node)
                self.nodeexpanded+=1
                self.end_node.append(current_state_object)
                del self.start_node[0]
                self.start_node.sort(key = lambda x:x.low_cost_depth,reverse=False)


def main():
    print("Welcome to 8 puzzle solver")
    print("choose the of algorithm \n1. Uniform Cost Search ""\n2. A* with the Misplaced Tile heuristic." "\n3. A* with the Manhattan distance heuristic\n")
    choose_algo = int(input())
    puzzle_type = input("Select the option from below:"+
                    "\n"+"1. Default Puzzle or 2.User Defined Puzzle \n")    #allowing the user to select the type of the puzzle      
    puzzle = int(puzzle_type)
    puzzle1 = [[[1, 2, 3], [4, 5, 6], [7, 8, 0]], [[1, 2, 3], [4, 0, 6], [7, 5, 8]], [[1, 2, 3], [5, 0, 6], [4, 7, 8]], [[1, 3, 6], [5, 0, 2], [4, 7, 8]], [[1, 3, 6], [5, 0, 7], [4, 8, 2]], [[1, 6, 7], [5, 0, 3], [4, 8, 2]], [[7, 1, 2], [4, 8, 5], [6, 3, 0]], [[0, 7, 2], [4, 6, 1], [3, 5, 8]]]
    puzzle = int(puzzle_type)
    if puzzle == 1: #if the user selects 1 i.e default puzzle this loop would execute
        print("Select the level of difficulty for the puzzle: 0, 2, 4 .. where 0 is the easiest with depth 0")
        difficult = int(input())
        puzzle_final = puzzle1[difficult]
    elif puzzle == 2:  #if the user selects 2 they would be allowed to give there own input                                                            
        puzzle_final=[]
        row = int(input("enter the number of rows for 8 puzzle"))
        column = int(input("enter the number of columns for 8 puzzle"))
        
        for i in range(3):
            print("Enter the user defined puzzle rowise and add 0 as blank space")
            row = list(map(int, input().split())) 
            puzzle_final.append(row)   

    print("initial puzzle: \n")
    print(puzzle_final)
    unsolved_puzzle =[]
    unsolved_puzzle_final = []
    count=0
    for i in puzzle_final:
        for j in i:
            unsolved_puzzle.append(str(j))
            count+=1
            if count == 3:
                count = 0
                unsolved_puzzle_final.append(unsolved_puzzle)
                unsolved_puzzle=[]

    print("\n")
    puz = Puzzle(3)
    puz.process(unsolved_puzzle_final, choose_algo)

main()