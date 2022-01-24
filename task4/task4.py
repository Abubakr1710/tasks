pointx1 = int(input(" To run the program you need to know 8  points of x,y,z of Cube-A and Cube-B. Please enter points of x one by one. If you want to continue press 8: "))
x1 = []
for i in range(pointx1):
    a = int(input())
    x1.append(a)

pointy1 = int(input("Please enter points of y one by one. If you want to continue press 8: "))
y1 = []
for i in range(pointy1):
    b = int(input())
    y1.append(b)

pointz1 = int(input("Please enter points of z one by one. If you want to continue press 8: "))
z1 = []
for i in range(pointz1):
    c = int(input())
    z1.append(c)

pointx2 = int(input("Warning you started points of Cube-B.Please enter points of x one by one. If you want to continue press 8: "))
x2 = []
for i in range(pointx2):
    d = int(input())
    x2.append(d)

pointy2 = int(input("Please enter points of y one by one. If you want to continue press 8: "))
y2 = []
for i in range(pointy2):
    e = int(input())
    y2.append(e)

pointz2 = int(input("Please enter points of z one by one. If you want to continue press 8: "))
z2 = []
for i in range(pointz2):
    f = int(input())
    z2.append(f)

print('Cube-A points:')
print(x1)
print(y1)
print(z1)

print('Cube-B points:')
print(x2)
print(y2)
print(z2)

if max(x1) > max(x2) or max(y1) > max(y2) or max(z1) > max(z2):
    print('1')
else:
    print('0')