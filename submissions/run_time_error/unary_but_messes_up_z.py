#! /usr/bin/env python3

x, y, z = map(int, input().split())
x_in_unary = '1'*x
y_in_unary = '1'*y
z_in_unary = '1'*z

while len(y_in_unary):
    x_in_unary += y_in_unary.pop()
while len(z_in_unary):
    x_in_unary += y_in_unary.pop()

print(len(x_in_unary))
