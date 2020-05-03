from hyperop import hyperop
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**1024,-1))
sys.setrecursionlimit(10**44)
f = int(input('\n'"Input f: "))
u = str(f-1)
c = str(f)+u
k = int(c)
H = hyperop(4)
s1 = 0
y = int(input('\n'"Input y: "))
    for f in range(f,k+1):
        j = H(f,f+1)
        if f == k:
            break
        s1 += j
s2 = H(s1,y+1)
        t = str(s2-1)
        o = str(s2)+t
        p = int(o)
        V = 0
        for s2 in range (s2,p+1):
            e = (H(s2,s2+1))
            if s2 == p:
                break
            V += e
print('\n' "V(f,y) = ", V)
