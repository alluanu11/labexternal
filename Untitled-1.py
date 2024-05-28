class waterjug:
    def __init__(self, jug6, jug2, target):
        self.jug6=jug6
        self.jug2=jug2
        self.target=target
        self.g=g
        self.h=h
        self.f=g+h
    def __it__(self,other):
        return self.f<other.f
    def __eq__(self,state):
        return self.f==state.f
    def heuristic(self,state):
        return abs(self.target-state.jug6)+abs(self.target-state.jug2)
   
    def solve(state):
        if state.jug6==state.target and state.jug2==state.target:
            return state
        
        
    def get_neighbours(self,goal):
        neighbours=[]
        if self.jug6>0:
            neighbours.append(waterjug(self.jug6-1,self.jug2,goal))
            if self.jug2>0:
                neighbours.append(waterjug(self.jug6,self.jug2-1,goal))
                return neighbours
initial_state = WaterJug(0, 0)
goal_state = WaterJug(4, 0)  
solution = a_star_search(initial_state, goal_state)
if solution:
    solution.print_path()
else:
    print("No solution found")




