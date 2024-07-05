# flake8: noqa
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

AB = float(input())
BC = float(input())

pi = math.pi

val = str( int(math.degrees((pi/2 - math.atan(BC/AB)))) )

print(val + chr(176))
