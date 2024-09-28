"""N = int(input())
K = int(input())

Get = K//N

K = K- Get

print(Get)

left= K%Get

print(left)
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
"""
"""
N = int(input())

if N % 2 == 0:

    K=N//2
    print(K)

else:
    K=N//2
    K=K+(K//2>0)
    print(K)
"""


