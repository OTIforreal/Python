"""N = int(input())

if N >=1:
    N=N<<1
    print(N)
elif N<=0:
    print("ERRORRRRRR")
    """
"""
print("First number - ")
N = int(input())
print("Second number - ")
K = int(input())

print("Chose operation(+,-,*,/) - ")

select = input()

if select == "+":
    res=N+K
    print(res)
elif select == "-":
        res = N - K
        print(res)
elif select == "*":
        res = N * K
        print(res)
elif select == "/":
        res = N / K
        print(res)

"""
"""
N = int(input())

K = N//1000
print(K)
K1= (N-K*1000)//100
print(K1)
K2= (N-K*1000-K1*100)//10
print(K2)
K3= (N-K*1000-K1*100-K2*10)
print(K3)
sum=K+K3
print(sum)
antisum=abs(K1-K2)
print(antisum)
if sum==antisum:
    print("yes")
else:
    print("no")
"""
"""
age=int(input())

if age>=18:
    print("Access is allowed")
elif age <= 18:
        print("Access denied")
"""
"""
N = int(input())
B = int(input())
L = int(input())

if N+N == B:
    if B + N == L:
        print("YES")
    else:
        print("NO")
else:
        print("NO")
"""
"""
x = int(input())

y = int(input())

xgo= int(input())

ygo= int(input())

if y==ygo and 1<=x<=8 or x==xgo and 1==y==8:

        print('YES')
else :

        print('NO')
"""
"""
x = int(input())

y = int(input())

xgo= int(input())

ygo= int(input())

if   x-1<= x<=x+1 or y-1==y==y+1:

        print('YES')
else :

        print('NO')
"""

"""
N = int(input())
B = int(input())
L = int(input())

if N<B<L:
    print(B)
elif N<L<B:
 print(L)
elif B > N > L:
 print(N)

"""



