## To keep the code clean from comments and use better notations, this is used instead.

```python
from hyperop import hyperop
```
A custom library for hyperoperator, used here for tetration

```python
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**1024,-1))
sys.setrecursionlimit(10**44)
```
Pretty self-explanatory, sets recursion depth and stack size (those numbers are absurdly large and random)
Resource only works on Unix, will errro out on Windows


