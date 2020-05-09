# Output in standard shell will not look pretty, if Jupyter notebook is available better use the .ipynb
from sympy import diff, symbols
import math
x, y, z = symbols('x y z')
f = input('\n'"Use --help to see how to input functions correctly. If you know what to do, type function directly."'\n')
if f == "--help":
    print("For multiplication, use *"'\n'"For exponentiation, use **"'\n'"For Nth roots, use **(1/n)"'\n'"Other variables are all the same as in normal math, i.e. sin, tan, etc."'\n'"!Don't forget to use brackets!")
else:
    k = (input('\n' "Derive with respect to which variable? "))
    n = int(input('\n'"How many times to derive? "))
    print('\n' "The result is: "'\n''\n',diff(f, k, n))
