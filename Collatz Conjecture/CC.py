n = int(input('\n'"Insert a number: "))
if n%2:
    print("Is odd")
else:
    print("Is even")
print("________________")
print("Starting..."'\n')
w = 0
while n != 1:
    if n%2 == 0:
        n = n//2
        print (n)
    else:
        n = 3*n+1
        print (n)
    w = w + 1
if n == 1:
        print('\n'"Returned to 1. Took", w, "steps to terminate, try again")
