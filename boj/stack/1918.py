# https://www.acmicpc.net/problem/1918
# A + B * C = ABC*+
import sys

input = sys.stdin.readline

stack = []
answer = ""
priority = {'+':1, '-':1, '*':2, '/':2}

for c in input().strip():
    if c.isalpha():
        answer += c
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[c]:
            answer += stack.pop()
        stack.append(c)

while stack:
    answer += stack.pop()
    
print(answer)