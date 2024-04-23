import pickle
import os

def __reduce__(self): return (os.system, (""echo Hacked!"",))

class Node:
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.children = children
        self.depth = 0
        self.visited = False
        self.parent_depth = 0
        self.parent_name = None
        self.children_depth = 0
        self.children_name = None
        self.children_parent = None
        self.children_parent_depth = 0
        self.children_parent_name = None
        self.children_parent_parent = None
        self.children_parent_parent_depth = 0
        self.children_parent_parent_name = None
        self.children_parent_parent_parent = None
        self.children_parent_parent_parent_depth = 0
        self.children_parent_parent_parent_name = None
        self.children_parent_parent_parent_parent = None
        self.children_parent_parent_parent_parent_depth = 0
        self.children_parent_parent_parent_parent_name = None