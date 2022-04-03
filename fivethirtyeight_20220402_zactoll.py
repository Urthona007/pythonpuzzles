'''"Zactoli" is a game where you start with the number 1 and then you can either
1) double the number
2) if the number is one more than an odd multiple of 3, you can subtract by 1 and
then divide by 3.

What is the lowest target number that cannot be reached?

'''

print(__doc__)

class Node:
    """A node represents a gamestate in relation to future and past gamestates.  A node has a
    parent node (unless it is the root node defied by the initial conditions).  The parent node,
    plus an action, generate a new gamestate and node.  A node can have up to 6 potential child
    nodes as a result of the 6 actions that can be performed."""
    action_name = ("Fil1", "Fil2", "Emp1", "Emp2", "1to2", "2to1")
    def __init__(self, value, parentnode=None):
        self.parentnode = parentnode
        self.value = value
        if parentnode:
            self.depth = parentnode.depth + 1
        else:
            self.depth = 1
#        self.double_or_reduce_node = ["UNTESTED", "UNTESTED"] # NOTE: a heterogenous list of stringe or Nodes.

    def __str__(self):
        return f"parentnode {self.parentnode.value} -> gamestate {self.value}"

    def __eq__(self, other):
        if not isinstance(self, Node) and not isinstance(other, Node):
            return True
        if not isinstance(other, Node):
            return False
        if self.value == other.value:
            return True
        return False

    def print_found(self):
        print(f"Target {self.value} FOUND at depth {self.depth}")
    #    if self.parentnode:
    #       self.parentnode.print_ancestors()

    def print_ancestors(self):
        print(f"L{self.depth} {self.value}")
        if self.parentnode:
            self.parentnode.print_ancestors()

def grow_node_list(target, node_list, max_depth):
    new_node_list = []
    MAXVAL = 100000
    for a_node in node_list:
        # print(f"{a_node.value}")
        double_node = Node(a_node.value*2, a_node)
        if double_node.depth == max_depth:
            print(f"Target {target} NOT FOUND! Max depth {max_depth} reached.")
            return False
        if double_node.value == target:
            double_node.print_found()
            return True
        if double_node.value < MAXVAL and double_node not in node_list:
            node_list.append(double_node)
        if (a_node.value - 1)%6 == 3:
            reduce_node = Node(int((a_node.value-1)/3), a_node)
            if reduce_node.value == target:
                reduce_node.print_found()
                return True
            if reduce_node not in node_list:
                node_list.append(reduce_node)
    return(f"Target {target} NOT FOUND!  No more eligible guesses.")
found = True
target = 1
start_max_depth = 60
while found:
    target += 1
    start_node_list = [Node(1),]
    found = grow_node_list(target, start_node_list, start_max_depth)

