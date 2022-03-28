'''Given two beakers, b1 and b2, of size s1 and s2 in liters, you need to exactly measure "goal"
liters.

Actions you can take are limited to six:
    Completely fill a beaker (Fil1, Fil2)
    Completely empty a beaker (Emp1, Emp2)
    Completely empty/fill one beaker to another with no spilling. (1to2, 2to1)

This program takes a range of values in liters for initializing beaker b2, and determines
    how many unique solutions exist for each initialization value,
    the solution(s) that requires the least number of actions for each initialization value,
    and which initialization value is therefore recommended.

The original Brilliant problem used s1 = 18, s2 = 15, goal = 12, and tested init values 8, 9, 10,
and 11.'''
import argparse

print(__doc__)

class Beaker:
    """A container that has a size and an amount of liquid in it."""

    def __init__(self, size, init_val):
        self.size = size
        self.amt = init_val

    def __eq__(self, other):
        if not isinstance(self, Beaker) and not isinstance(other, Beaker):
            return True
        if not isinstance(other, Beaker):
            return False
        if self.size == other.size and self.amt == other.amt:
            return True
        return False

class GameState:
    """Defines 2 beakers."""
    def __init__(self, beaker1_sz, beaker1_init, beaker2_sz, beaker2_init):
        self.beaker = [Beaker(beaker1_sz, beaker1_init), Beaker(beaker2_sz, beaker2_init)]

    def __str__(self):
        return f"({self.beaker[0].amt},{self.beaker[1].amt})"

class Node:
    """A node represents a gamestate in relation to future and past gamestates.  A node has a
    parent node (unless it is the root node defied by the initial conditions).  The parent node,
    plus an action, generate a new gamestate and node.  A node can have up to 6 potential child
    nodes as a result of the 6 actions that can be performed."""
    action_name = ("Fil1", "Fil2", "Emp1", "Emp2", "1to2", "2to1")
    def __init__(self, gamestate, parentnode=None):
        self.parentnode = parentnode
        self.gamestate = gamestate
        self.fill_empty_or_pour_child_node = ["UNTESTED", "UNTESTED", "UNTESTED", "UNTESTED", \
            "UNTESTED", "UNTESTED"] # NOTE: a heterogenous list of stringe or Nodes.

    def __str__(self):
        return f"parentnode {self.parentnode.gamestate} -> gamestate {self.gamestate}"

    def __eq__(self, other):
        if not isinstance(self, Node) and not isinstance(other, Node):
            return True
        if not isinstance(other, Node):
            return False
        if self.gamestate.beaker[0] == other.gamestate.beaker[0] and \
            self.gamestate.beaker[1] == other.gamestate.beaker[1]:
            return True
        return False

    def print_terminating_threads(self, prefix = "", goal_results = None):
        """A recursive function.  If goal_results is set, it quietly gathers all end nodes on a
        tree.  Otherwise will print each line.  Useful for debugging and/or evaluating the results
        in a node tree."""
        for n, cnode in enumerate(self.fill_empty_or_pour_child_node):
            if isinstance(cnode, Node):
                cnode.print_terminating_threads(f"{prefix} {self.gamestate} -> "
                    f"{Node.action_name[n]} ->", goal_results=goal_results)
            elif cnode[-6:] == "GOAL!!":
                result = f"{prefix} {self.gamestate} : {cnode}"
                num_actions = 0
                for act in Node.action_name:
                    num_actions += result.count(act)
                goal_string = f"GOAL achieved in {num_actions} moves: {result}"
                if goal_results is None:
                    print(goal_string)
                else:
                    goal_results.append((num_actions, goal_string))

    def grow(self, goal):
        """A recursive function that expands the node tree, finding all unique solutions and
        deadends."""
        for n, cnode in enumerate(self.fill_empty_or_pour_child_node):
            # If an action can make a valid node, instantiate it
            if cnode == "UNTESTED":
                if n == 0: # Fill1
                    if self.gamestate.beaker[0].amt < self.gamestate.beaker[0].size:
                        cnode = Node(GameState(self.gamestate.beaker[0].size, \
                            self.gamestate.beaker[0].size, self.gamestate.beaker[1].size, \
                                self.gamestate.beaker[1].amt), self)
                        action = Node.action_name[n]
                    else:
                        cnode = "Ful1"
                elif n == 1: # Fill2
                    if self.gamestate.beaker[1].amt < self.gamestate.beaker[1].size:
                        cnode = Node(GameState(self.gamestate.beaker[0].size, \
                            self.gamestate.beaker[0].amt, self.gamestate.beaker[1].size, \
                                self.gamestate.beaker[1].size), self)
                        action = Node.action_name[n]
                    else:
                        cnode = "Ful2"
                elif n == 2: # Emp1
                    if self.gamestate.beaker[0].amt > 0:
                        cnode = Node(GameState(self.gamestate.beaker[0].size, 0, \
                            self.gamestate.beaker[1].size, self.gamestate.beaker[1].amt), self)
                        action = Node.action_name[n]
                    else:
                        cnode = "Zer1"
                elif n == 3: # Emp2
                    if self.gamestate.beaker[1].amt > 1:
                        cnode = Node(GameState(self.gamestate.beaker[0].size, \
                            self.gamestate.beaker[0].amt, self.gamestate.beaker[1].size, 0), \
                                self)
                        action = Node.action_name[n]
                    else:
                        cnode = "Zer2"
                elif n == 4: # 1to2
                    if self.gamestate.beaker[0].amt > 0 and \
                        self.gamestate.beaker[1].amt != self.gamestate.beaker[1].size:
                        if self.gamestate.beaker[0].amt > \
                            (self.gamestate.beaker[1].size - self.gamestate.beaker[1].amt):
                            amt = self.gamestate.beaker[1].size - self.gamestate.beaker[1].amt
                        else:
                            amt = self.gamestate.beaker[0].amt
                        cnode = Node(GameState(self.gamestate.beaker[0].size, \
                            self.gamestate.beaker[0].amt - amt, self.gamestate.beaker[1].size, \
                                self.gamestate.beaker[1].amt + amt), self)
                        action = Node.action_name[n]
                    else:
                        cnode = "No12"
                elif n == 5: # 2to1
                    if self.gamestate.beaker[1].amt > 0 and \
                        self.gamestate.beaker[0].amt != self.gamestate.beaker[0].size:
                        if self.gamestate.beaker[1].amt > \
                            (self.gamestate.beaker[0].size - self.gamestate.beaker[0].amt): \
                            amt = self.gamestate.beaker[0].size - self.gamestate.beaker[0].amt
                        else:
                            amt = self.gamestate.beaker[1].amt
                        cnode = Node(GameState(self.gamestate.beaker[0].size, \
                            self.gamestate.beaker[0].amt + amt, self.gamestate.beaker[1].size, \
                                self.gamestate.beaker[1].amt - amt), self)
                        action = Node.action_name[n]
                    else:
                        cnode = "No21"

                self.fill_empty_or_pour_child_node[n] = cnode
                if isinstance(cnode, Node):
                    if goal in (cnode.gamestate.beaker[0].amt, \
                        cnode.gamestate.beaker[1].amt):
                        self.fill_empty_or_pour_child_node[n] = cnode = \
                            f'{action} -> {cnode.gamestate} : GOAL!!'
                    elif cnode.is_unique():
                        cnode.grow(goal)
                    else:
                        self.fill_empty_or_pour_child_node[n] = cnode = \
                            f'{action} -> {cnode.gamestate} : REPEAT'

    def _no_match_prev(self, g_state):
        """Utility function for is_unique()."""
        if isinstance(self, Node) and isinstance(g_state, GameState):
            if self.gamestate.beaker[0] == g_state.beaker[0] and \
                self.gamestate.beaker[1] == g_state.beaker[1]:
                return False
            if self.parentnode is not None and isinstance(self.parentnode, Node):
                return self.parentnode._no_match_prev(g_state)
            return True
        else:
            print("shouldnt be here")
            assert True
            return False

    def is_unique(self):
        """ See if a new node.gamestate matches one its ancestors."""
        if self.parentnode is None:
            return True
        assert isinstance(self.parentnode, Node)
        return self.parentnode._no_match_prev(self.gamestate)

def solve(args):
    """ Main work function."""
    # pylint: disable=C0103
    best_initialization = 10000
    best_initialization_solution = None
    for beaker2_initval in range(args.bucket_2_test_start_range_low, \
        args.bucket_2_test_start_range_high+1):
        gs = GameState(args.bucket_1_size, 0, args.bucket_2_size, beaker2_initval)
        print(f"\n *** For beaker starting value {beaker2_initval} {gs} ***")

        # Make a node map and then grow it.
        root_node = Node(gs)
        root_node.grow(args.goal)

        goal_results_list = []
        root_node.print_terminating_threads(goal_results = goal_results_list)

        print(f"{len(goal_results_list)} unique solutions found.")

        best_result_level = 10000
        best_result_string_list = ["No Goal found",]
        for results in goal_results_list:
            if results[0] < best_result_level:
                best_result_level = results[0]
                best_result_string_list = [results[1], ]
            elif results[0] == best_result_level:
                best_result_string_list.append(results[1])

        if not len(best_result_string_list):
            print("No GOAL solutions found!")
        else:
            add_s = 's'
            was_were = "were"
            if len(best_result_string_list) == 1:
                add_s = ''
                was_were = "was"
            print(f"{len(best_result_string_list)} best solution{add_s} requiring only "
                f"{best_result_level} actions {was_were} found:")
            for best_result in best_result_string_list:
                print(f"\t{best_result}")
            if best_result_level < best_initialization:
                best_initialization_solution = f"Initializing beaker 2 to {beaker2_initval} " + \
                    f"is the best solution and requires only {best_result_level} actions to " + \
                    f"achieve the goal of {args.goal}."
                best_initialization = best_result_level
            elif best_result_level == best_initialization:
                best_initialization_solution = best_initialization_solution[:25] + \
                    f"{beaker2_initval} or " + best_initialization_solution[25:]

    print(f"\n*** {best_initialization_solution} ***")

# Main code
parser = argparse.ArgumentParser()
parser.add_argument("bucket_1_size", type=int)
parser.add_argument("bucket_2_size", type=int)
parser.add_argument("goal", type=int)
parser.add_argument("bucket_2_test_start_range_low", type=int)
parser.add_argument("bucket_2_test_start_range_high", type=int)
my_args = parser.parse_args()

solve(my_args)
