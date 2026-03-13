import time
start = time.time()
# Top down approach 
def fibo(n,dp):
    if n == 0 or n == 1:
        return n
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
        return dp[n]
n = 100
dp = [-1 for x in range(n+1)]
print("answer:-",fibo(n,dp))

print("bottomup",time.time()-start)


start = time.time()
# Bottom up approach 
def fibo(n):
    mid = 0
    prev = 1
    out = mid + prev
    while n-1:
        n -= 1
        prev = mid 
        mid = out 
        out = mid + prev
    return out

print("answer:-",fibo(100))

print("topdown:-",time.time() - start)
