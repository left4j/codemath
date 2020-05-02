from hyperop import hyperop
import sys
import resource
# resorce only works on Unix, will error out on Windows
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**7)
# probably even with such a high recursion limit and
# stack size nothing above 3 will ever really compute
# unless ran on a supercomputer
print('\n'"Input an integer greater than or equal to 1:")
n = int(input())
x = str(n-1)
r = str(n)+x
y = int(r)
# this hacky shit is used to get the notation of the power
# "coming down" (mentioned in the respective doc) for n^n-1
H = hyperop(4)
s = 0
for n in range(n,y):
    j = H(n,n)
    s += j
print('\n'"Result:")
print(s)
# Due to how tetration works, gotta put n+1 insead of n number of iterations 
# to achieve the desired resut e.g. 3^3^3^3 should be written as H(3,4). So 
# in this case you have to write n+1 to elevate n to itself n times