# Definition for a binary tree node.
# flake8: noqa

# problem : https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/




from queue import Queue
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

inpu = input().strip('[').strip(']').split(',')
# inp = ['2','3','1','3','1','null','1']
inp = []
for n in inpu:
  if n == 'null' or n == '':
    inp.append(None)
  else:
    inp.append(int(n))
tree_node = None
parent_nodes = Queue()

tree_node = Node(val=inp.pop(0))
parent_nodes.put(tree_node)

while len(inp) > 0:
  parent = parent_nodes.get_nowait()
  left = inp.pop(0)
  if left:
    parent.left = Node(val=left)
  right = inp.pop(0)
  if right:
    parent.right = Node(val=right)

  parent_nodes.put(parent.left)
  parent_nodes.put(parent.right)


traverse_paths = []

def DFS_traverse(node: Node, path: list):
  if node:
    path.append(node.val)
    if node.left is None and node.right is None:
      traverse_paths.append(path.copy())
    DFS_traverse(node=node.left, path=path)
    DFS_traverse(node=node.right, path=path)

    path.pop()


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[Node]) -> int:
        DFS_traverse(node=root, path=[])
        cnt = 0
        for path in traverse_paths:
            odds = set()
            path.sort()
            for node in path:
                if node in odds:
                    odds.remove(node)
                else:
                    odds.add(node)
            
            if len(odds) <= 1:
                cnt += 1
        return cnt

Solution().pseudoPalindromicPaths(root=tree_node)




