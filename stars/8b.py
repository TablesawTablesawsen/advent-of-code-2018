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

    def node_value(self):
        if self.child_count == 0:
            return sum(self.metadata)
        else:
            return sum(self.children[i-1].node_value() for i in self.metadata if i <= len(self.children))        

with open('input/day8.txt') as input:
    node_input = ( int(x) for x in next(input).split() )

root = Node(node_input)
print(root.node_value())