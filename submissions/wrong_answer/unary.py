#! /usr/bin/env python3

x, y, z = map(int, input().split())
x_in_unary = '1'*x
y_in_unary = '1'*y
z_in_unary = '1'*z

while len(y_in_unary):
    x_in_unary += y_in_unary[-1]
    y_in_unary = y_in_unary[:-1]
while len(z_in_unary):
    x_in_unary += z_in_unary[-1]
    z_in_unary = z_in_unary[:-1]

print(len(x_in_unary))
