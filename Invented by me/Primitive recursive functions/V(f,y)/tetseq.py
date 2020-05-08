from hyperop import hyperop
f = int(input('\n'"Input f: "))
u = str(f-1)
c = str(f)+u
k = int(c)
H = hyperop(4)
y = int(input('\n'"Input y: "))
s1 = 0
for f in range(f,k+1):
   s1 += H(f,f+1)
s2 = H(s1,y+1)
t = str(s2-1)
o = str(s2)+t
p = int(o)
e = 0
for s2 in range (s2,p+1):
    e += H(s2,s2+1)
SN = input('\n'"Convert output to scientific notation? Answer y/n")
if SN == "y":
    V = decimal.Context(prec=3).create_decimal(e)
elif SN == "n":
    V = e
print('\n' "V(f,y) = ", V)
