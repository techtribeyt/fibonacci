#Fibonacci: F(1)=F(2)=1, F(n)=F(n-1)+F(n-2)
import time

# simple (inefficient) approach - exponential
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)

# dynamic programming (effcient) - polynomial
def fib2(n):
    f = [0]*(n+1)
    f[0]=1
    f[1]=1
    for i in range(2, n+1, 1):
        f[i]=f[i-1]+f[i-2]
    return f[n]

'''t1 = time.time()
print(fib(35))
print("Fib1 time spent: " + str(time.time()-t1))'''

t1 = time.time()
print(fib2(350))
print("Fib2 time spent: " + str(time.time()-t1))
