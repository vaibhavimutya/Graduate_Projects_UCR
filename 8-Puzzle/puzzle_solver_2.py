class Child:
    def __init__(self,puzzle,depth,low_cost_depth):
        self.puzzle = puzzle
        self.depth = depth
        self.low_cost_depth = low_cost_depth

    def node_expand(self):
            current_node_puzzle,value = self.find(self.puzzle,'0')
            val_list = [[current_node_puzzle,value-1],[current_node_puzzle,value+1],[current_node_puzzle-1,value],[current_node_puzzle+1,value]]
            children = []
            for val in val_list:
                child = self.tile_slide(self.puzzle,current_node_puzzle,value,val[0],val[1])
                if child is not None:
                    child_node = Child(child,self.depth+1,0)
                    children.append(child_node)
            return children
            
    def tile_slide(self,current_puzzle,row_index_1,column_index_1,row_index_2,column_index_2):
        if row_index_2 >= 0 and row_index_2 < len(self.puzzle) and column_index_2 >= 0 and column_index_2 < len(self.puzzle):
            temp_puzzle = self.copy(current_puzzle)
            temp = temp_puzzle[row_index_2][column_index_2]
            temp_puzzle[row_index_2][column_index_2] = temp_puzzle[row_index_1][column_index_1]
            temp_puzzle[row_index_1][column_index_1] = temp
            return temp_puzzle
        else:
            return None
    
    def copy(self,base):
            lst = []
            for s in base:
                t = []
                for r in s:
                    t.append(r)
                lst.append(t)
            return lst    
                
    def find(self,current_puzzle,target):
        for x in range(0,len(self.puzzle)):
            for y in range(0,len(self.puzzle)):
                if current_puzzle[x][y] == target:
                    return x,y