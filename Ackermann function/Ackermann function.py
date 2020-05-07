'''
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**64,-1))
sys.setrecursionlimit(10**9)
Kinda useless, will just leave here for whatever's sake
'''
j = int(input('\n'"Enter m: "))
k = int(input("Enter n: "))
print('\n'"A(4,2) and above will not work, unless ran on a supercomputer")
def A(m,n):
    if m==0:
        return n+1
    elif n==0 and m>0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))

print('\n'"Result:", A(j,k))
