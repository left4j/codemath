## To keep the code clean from comments and use better notations, this is used instead.
### Written in case I forget what the code means

```python
from hyperop import hyperop
```
A custom library for hyperoperator, used here for tetration
<br>

```python
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**1024,-1))
sys.setrecursionlimit(10**44)
```
Pretty self-explanatory, sets recursion depth and stack size (those numbers are absurdly large and random). Resource only works on Unix, will errro out on Windows
<br>
```python
f = int(input('\n'"Input f: "))
u = str(f-1)
c = str(f)+u
k = int(c)
```
Hacky shit used to achieve the ^↓ described in the definition file
<br>
```python
H = hyperop(4)
s1 = 0
y = int(input('\n'"Input y: "))
for f in range(f,k+1):
  j = H(f,f+1)
  if f == k:
    break
  s1 += j
```
Define tetration, get user to input y (better here, before the sequence starts computing),
start a loop going from f to ^↓(f^f-1) in which a sequence with exponential towers is computed.
<br>
```python
s2 = H(s1,y+1)
```
Take sum of the sequence, create a tetration tower of size y
(Due to how tetration works, gotta put y+1 insead of y number of iterations 
to achieve the desired resut e.g. 3^3^3^3 should be written as H(3,4). So 
in this case you have to write y+1 to elevate s2 to itself y times. Same goes for f before that.)
<br>
```python
t = str(s2-1)
o = str(s2)+t
p = int(o)
```
Same stuff as before
<br>
```python
V = 0
for s2 in range (s2,p+1):
  e = (H(s2,s2+1))
  if s2 == p:
    break
  V += e
```
Sum of the sequence for s2
<br>
```python
print('\n' "V(f,y) = ", V)
```
Final output of V(f,y)



