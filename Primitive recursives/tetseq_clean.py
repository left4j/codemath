from hyperop import hyperop
import sys
import resource
# resorce only works on Unix, will error out on Windows
resource.setrlimit(resource.RLIMIT_STACK, (2**1024,-1))
sys.setrecursionlimit(10**44)
# probably even with such a high recursion limit and
# stack size nothing above 3 will ever really compute
# unless ran on a supercomputer
f = int(input('\n'"Input f: "))
u = str(f-1)
c = str(f)+u
k = int(c)
# this hacky shit is used to get the notation of the power
# "coming down" (mentioned in the respective doc) for n^n-1
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
            if s == p:
                break
            V += e
print('\n' "V(f,y) = ", V)
# Due to how tetration works, gotta put n+1 insead of n number of iterations 
# to achieve the desired resut e.g. 3^3^3^3 should be written as H(3,4). So 
# in this case you have to write n+1 to elevate n to itself n times

# now the same rules apply as in the last sequence, but
# now on the sum of that sequence (s), then it gets summed again
# that's the final output
