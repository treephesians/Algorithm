# https://www.acmicpc.net/problem/1991
import sys

input = sys.stdin.readline

N = int(input())
matrix = {}

for _ in range(N):
    parent, left_child, right_child = input().split()
    matrix[parent] = [left_child, right_child]

def preorder_traversal(node):
    if node != '.':
        print(node, end='')
        preorder_traversal(matrix[node][0])
        preorder_traversal(matrix[node][1])

def inorder_traversal(node):
    if node != '.':
        inorder_traversal(matrix[node][0])
        print(node, end='')
        inorder_traversal(matrix[node][1])

def postorder_traversal(node):
    if node != '.':
        postorder_traversal(matrix[node][0])
        postorder_traversal(matrix[node][1])
        print(node, end='')

preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')
