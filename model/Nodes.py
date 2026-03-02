import numpy as py
from typing import List, Optional


class Node:
    def __init__(self,
                 weights: Optional[List[float]] = None,
                 bias: float = 0.0):
        self.weights: List[float] = weights
        self.bias: float = bias
        self.children: List["Node"] = []
        self.parents: List["Node"] = []
        self.name: str = ''

    def append_child(self, child: "Node"):
        self.children.append(child)
        child.parents.append(self)

    def to_string(self):
        return(
            f'weights={self.weights}, bias={self.bias}'
        )
