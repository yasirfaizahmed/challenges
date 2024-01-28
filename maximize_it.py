# flake8: noqa
from fractions import Fraction

inp = input()
N = int(inp.split(' ')[0])
M = int(inp.split(' ')[1])
# N = int(input())
# M = int(input())

max_vals = []
for _ in range(N):
    lis = list(input().split(' '))
    new_lis = []
    for val in lis:
        new_lis.append(int(val))
    max_vals.append(max(new_lis))

res = 0
for val in max_vals:
    res += (val * val)

print(res%M)