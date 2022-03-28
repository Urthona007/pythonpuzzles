''' You need to measure "goal" (12) and you have two containers:
    "beaker" #1 (18) (empty)
    "beaker" #2 (15) (starts w/ 8, 9, 10, 11)  <== which starting condition is quickest to goal
    Actions available:
    Completely fill a beaker
    Completely empty a beaker
    Completely empty/fill one beaker to another
    '''

from pickle import FALSE
from typing import ClassVar


print(__doc__)

class beaker:
    def __init__(self, size, init_val):
        self.size = size
        self.amt = init_val

    def __eq__(self, other):
        if not isinstance(self, beaker) and not isinstance(other, beaker):
            return True
        elif not isinstance(other, beaker):
            return False
        elif self.size == other.size and self.amt == other.amt:
            return True
        else:
            return False

class gamestate:
    def __init__(self, beaker1_sz, beaker1_init, beaker2_sz, beaker2_init):
        self.beaker = [beaker(beaker1_sz, beaker1_init), beaker(beaker2_sz, beaker2_init)]

    def __str__(self):
#        return f"{self.beaker[0].amt}/{self.beaker[0].size} {self.beaker[1].amt}/{self.beaker[1].size}"
        return f"({self.beaker[0].amt},{self.beaker[1].amt})"

class node:
    action_name = ("Fil1", "Fil2", "Emp1", "Emp2", "1to2", "2to1")
    def __init__(self, gamestate, parentnode=None):
        self.parentnode = parentnode
        self.gamestate = gamestate
        self.fill_empty_or_pour_child_node = ["UNTESTED", "UNTESTED", "UNTESTED", "UNTESTED", "UNTESTED", "UNTESTED"]

    def __str__(self):
        return(f"parentnode {self.parentnode.gamestate} -> gamestate {self.gamestate}")

    def __eq__(self, other):
        if not isinstance(self, node) and not isinstance(other, node):
            return True
        elif not isinstance(other, node):
            return False
        elif self.beaker[0] == other.beaker[0] and self.beaker[1] == other.beaker[1]:
            return True
        else:
            return False

    def print_terminating_threads(self, prefix = "", goal_results = None):     
        for n, cnode in enumerate(self.fill_empty_or_pour_child_node):
            if isinstance(cnode, node):
                cnode.print_terminating_threads(f"{prefix} {self.gamestate} -> {node.action_name[n]} ->", goal_results=goal_results)
#            else:
#                print(f"{prefix} {self.gamestate} : {self.fill_empty_or_pour_child_node[n]}")
            elif cnode[-6:] == "GOAL!!":
                result = f"{prefix} {self.gamestate} : {cnode}"
                num_actions = 0
                for act in node.action_name:
                    num_actions += result.count(act)
                goal_string = f"GOAL achieved in {num_actions} moves: {result}"
                if goal_results is None:
                    print(goal_string)
                else:
                    goal_results.append((num_actions, goal_string))

    def grow(self, goal):
        for n, cnode in enumerate(self.fill_empty_or_pour_child_node):
            if cnode == "UNTESTED":
                    if n == 0:
                        if self.gamestate.beaker[0].amt < self.gamestate.beaker[0].size:
                            cnode = node(gamestate(self.gamestate.beaker[0].size, self.gamestate.beaker[0].size, self.gamestate.beaker[1].size, self.gamestate.beaker[1].amt), self)
                            action = node.action_name[n]
                        else:
                            cnode = "Ful1"
                    elif n == 1:    
                        if self.gamestate.beaker[1].amt < self.gamestate.beaker[1].size:
                            cnode = node(gamestate(self.gamestate.beaker[0].size, self.gamestate.beaker[0].amt, self.gamestate.beaker[1].size, self.gamestate.beaker[1].size), self)
                            action = node.action_name[n]
                        else:
                            cnode = "Ful2"
                    elif n == 2:
                        if self.gamestate.beaker[0].amt > 0:
                            cnode = node(gamestate(self.gamestate.beaker[0].size, 0, self.gamestate.beaker[1].size, self.gamestate.beaker[1].amt), self)
                            action = node.action_name[n]
                        else:
                            cnode = "Zer1"
                    elif n == 3:
                        if self.gamestate.beaker[1].amt > 1:
                            cnode = node(gamestate(self.gamestate.beaker[0].size, self.gamestate.beaker[0].amt, self.gamestate.beaker[1].size, 0), self)
                            action = node.action_name[n]
                        else:
                            cnode = "Zer2"
                    elif n == 4:
                        if self.gamestate.beaker[0].amt > 0 and self.gamestate.beaker[1].amt != self.gamestate.beaker[1].size:
                            if self.gamestate.beaker[0].amt > (self.gamestate.beaker[1].size - self.gamestate.beaker[1].amt):
                                amt = self.gamestate.beaker[1].size - self.gamestate.beaker[1].amt
                            else:
                                amt = self.gamestate.beaker[0].amt
                            cnode = node(gamestate(self.gamestate.beaker[0].size, self.gamestate.beaker[0].amt - amt, self.gamestate.beaker[1].size, self.gamestate.beaker[1].amt + amt), self)
                            action = node.action_name[n]
                        else:
                            cnode = "No12"
                    elif n == 5:
                        if self.gamestate.beaker[1].amt > 0 and self.gamestate.beaker[0].amt != self.gamestate.beaker[0].size:
                            if self.gamestate.beaker[1].amt > (self.gamestate.beaker[0].size - self.gamestate.beaker[0].amt):
                                amt = self.gamestate.beaker[0].size - self.gamestate.beaker[0].amt
                            else:
                                amt = self.gamestate.beaker[1].amt
                            cnode = node(gamestate(self.gamestate.beaker[0].size, self.gamestate.beaker[0].amt + amt, self.gamestate.beaker[1].size, self.gamestate.beaker[1].amt - amt), self)
                            action = node.action_name[n]
                        else:
                            cnode = "No21"

                    self.fill_empty_or_pour_child_node[n] = cnode
#                    print(cnode)
                    if isinstance(cnode, node):
                        if cnode.gamestate.beaker[0].amt == goal or cnode.gamestate.beaker[1].amt == goal:
                            self.fill_empty_or_pour_child_node[n] = cnode = f'{action} -> {cnode.gamestate} : GOAL!!'
                        elif cnode.is_unique():
                            cnode.grow(goal)
                        else:
                            self.fill_empty_or_pour_child_node[n] = cnode = f'{action} -> {cnode.gamestate} : REPEAT'  
    
    def no_match_prev(self, gs):
        if isinstance(self, node) and isinstance(gs, gamestate):
            if self.gamestate.beaker[0] == gs.beaker[0] and self.gamestate.beaker[1] == gs.beaker[1]:
                return False
            elif self.parentnode is not None:
                return self.parentnode.no_match_prev(gs)
            else:
                return True
        else:
            print("shouldnt be here")
    
    def is_unique(self):
        if self.parentnode == None:
            return True
        return self.parentnode.no_match_prev(self.gamestate)

# Main code
goal = 12
beaker1_sz = 18
beaker2_sz = 15
best_initialization = 10000
best_initialization_solution = None
for beaker2_init in range(8, 12):
    gs = gamestate(beaker1_sz, 0, beaker2_sz, beaker2_init)
    print(f"\n *** For beaker starting value {beaker2_init} {gs} ***")

    # Make a node map and then grow it.
    root_node = node(gs)
    root_node.grow(goal)

    goal_results_list = []
    root_node.print_terminating_threads(goal_results = goal_results_list)

    print(f"{len(goal_results_list)} solutions found.")

    best_result_level = 10000
    best_result_string_list = ["No Goal found",]
    for results in goal_results_list:
        if results[0] < best_result_level:
            best_result_level = results[0]
            best_result_string_list = [results[1], ]
        elif results[0] == best_result_level:
            best_result_string_list.append(results[1])
    
    if not len(best_result_string_list):
        "No GOAL solutions found!"
    else:
        print(f"{len(best_result_string_list)} best solutions requiring only {best_result_level} actions were found:")
        for best_result in best_result_string_list:
            print(f"\t{best_result}")
        if best_result_level < best_initialization:
            best_initialization_solution = f"Initializing beaker 2 to {beaker2_init} is the best solution and requires only {best_result_level} actions to achieve the goal of {goal}."
            best_initialization = best_result_level
        elif best_result_level == best_initialization:
            best_initialization_solution = best_initialization_solution[:25] + f"{beaker2_init} or " + best_initialization_solution[25:]
    
print(f"\n*** {best_initialization_solution} ***")
