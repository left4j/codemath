import math
print("Input an integer greater than or equal to 1:")
n = int(input())
x = str(n-1)
r = str(n)+x
y = int(r)
print("Sequence starts:")
print(pow(n,n))
for n in range(n, y):
 print(pow(n+1,pow(n,n)))