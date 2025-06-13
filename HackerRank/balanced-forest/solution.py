#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

class Node:
    def __init__(self, data):
        self.children = []
        self.data = data
        self.acc = 0

def balancedForest(c, edges):
    root = createTree(c, edges)
    return findMinBalanceNode(root)

def createTree(c, edges):
    nodes = [Node(data) for data in c]
    for edge in edges:
        nodes[edge[0] - 1].children.append(nodes[edge[1] - 1])
        # There are some edges where child is in [0] and parent in [1]
        nodes[edge[1] - 1].children.append(nodes[edge[0] - 1])
    cleanTree(nodes[0])
    calculateAcc(nodes[0])
    return nodes[0]

# Removes links childs to parents
def cleanTree(root):
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        for child in curr.children:
            child.children.remove(curr)
            stack.append(child)

def calculateAcc(root):
    stack = []
    visited = set()
    stack.append(root)
    while stack:
        curr = stack.pop()
        if curr in visited:
            curr.acc += curr.data
            for child in curr.children:
                curr.acc += child.acc
        else:
            visited.add(curr)
            stack.append(curr)
            for child in curr.children:
                stack.append(child)

def findMinBalanceNode(root):
    total = root.acc

    # Limits of the accumulated values that could be splited
    # For example having total 12, min limit would be 4 and max limit 6
    min_limit = -(total // -3)
    max_limit = total // 2
    
    visited = set()
    stack = []
    stack.append(root)

    # This contains already visited accumulated values that are between the limits
    possible_acc = set()
    # This contains non-existent or unvisited accumulated values that are between the limits
    possible_comp = set()
    # Contains the complements of the parent nodes
    parents_comp = set()
    # Contains the accumulated values of the parent nodes
    parents_acc = set()

    min_node = math.inf
            
    while stack:
        curr = stack.pop()
        comp = total - curr.acc
        if curr not in visited:
            visited.add(curr)
            stack.append(curr)
            for child in curr.children:
                stack.append(child)

            if curr.acc <= max_limit and curr.acc >= min_limit:
                # curr.acc in possible_acc: 
                #        (1)
                #       /   \
                #     (2)   (2)
                # curr.acc in possible_comp
                #        (2)
                #       /   \
                #     (1)   (2)
                # 2 * curr.acc in parents_acc
                #        (1)
                #         |
                #        (2)
                #         |
                #        (2)
                # curr.acc in parents_comp
                #        (2)
                #         |
                #        (1)
                #         |
                #        (2)
                if curr.acc in possible_acc or curr.acc in possible_comp or 2 * curr.acc in parents_acc or curr.acc in parents_comp:
                    node = 3 * curr.acc - total
                    if min_node > node:
                        min_node = node
            elif curr.acc < min_limit and comp % 2 == 0:
                possible = comp / 2
                # possible + curr.acc in parents_acc
                #        (2)
                #         |
                #        (2)
                #         |
                #        (1)
                # possible in possible_acc
                #        (2)
                #       /   \
                #     (2)   (1)
                if possible + curr.acc in parents_acc or possible in possible_acc:
                    node = 3 * possible - total
                    if min_node > node:
                        min_node = node
            parents_comp.add(comp)
            parents_acc.add(curr.acc)
        else:
            parents_comp.remove(comp)
            parents_acc.remove(curr.acc)
            if curr.acc <= max_limit and curr.acc >= min_limit:
                possible_acc.add(curr.acc)
            elif curr.acc < min_limit and comp % 2 == 0 and comp / 2 not in parents_acc:
                possible_comp.add(comp / 2)

    return -1 if min_node == math.inf else int(min_node)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()

100

