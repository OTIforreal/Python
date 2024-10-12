x = int(input())
a = x // 1000
b = (x % 1000) // 100
c = (x % 100) // 10
d = (x % 10)
if a + d == b - c : print("yes")
else: print("no")
