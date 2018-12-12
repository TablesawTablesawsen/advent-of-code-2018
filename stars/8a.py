import itertools

class Node(object):
    """docstring for Node"""
    def __init__(self, input):
        self.child_count = next(input)
        self.metadata_count = next(input)
        self.children = [Node(input) for x in range(self.child_count)]
        self.metadata = [next(input) for x in range(self.metadata_count)]

    def metada_sum(self):
        return sum(self.metadata) + sum(node.metada_sum() for node in self.children)
        

with open('input/day8.txt') as input:
    node_input = ( int(x) for x in next(input).split() )

root = Node(node_input)
print(root.metada_sum())