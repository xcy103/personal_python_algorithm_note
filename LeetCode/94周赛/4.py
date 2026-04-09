from bisect import bisect_left


def lenLongestFibSubseq(arr) -> int:
    n = len(arr)
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            s = arr[i]+arr[j]
            f1 = i
            f2 = j
            idx = bisect_left(arr,s,j+1)
            l = 2
            while idx<n and arr[idx]==s:
                l+=1
                s-=arr[f1]
                s+=arr[idx]
                f1,f2 = f2,idx
                idx = bisect_left(arr,s,j+1)
            ans = max(l,ans)
    return ans
lenLongestFibSubseq([1,2,3,4,5,6,7,8])