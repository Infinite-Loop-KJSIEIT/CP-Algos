import sys
sys.setrecursionlimit(10**8)
dp_before=[0]
dp_cur=[0]

def C(i,j):
    return

def compute(l,r,optl,optr):
    if l>r:
        return
    mid=(l+r)>>1
    best=[(10**19,-1)]
    k=optl
    while k<=min(mid,optr):
        best = min(best, ((dp_before[k - 1] if k else 0) + C(k, mid), k))
        k+=1

    dp_cur[mid]=best[0]
    opt=best[1]
    compute(l, mid - 1, optl, opt)
    compute(mid + 1, r, opt, optr)

def solve(m,n):
    dp_before=[0]*n
    dp_cur=[0]*n
   
    
    for i in range(n):
        dp_before[i]=C(0,i)
    
    for i in range(m):
        compute(0, n-1, 0, n-1)
        dp_before=dp_cur


