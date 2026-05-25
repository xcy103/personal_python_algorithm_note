#就是总的方案数减去大于1的公约数的方案数，最后剩下的就是互质的方案数了
class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        mod = 10**9+7
        mx = max(map(max,mat))

        cnt = [0]*(mx+1)

        for i in range(mx,0,-1):

            res = 1
            for row in mat:
                c = 0
                for x in row:
                    if x%i==0:
                        c+=1
                if c==0:
                    res = 0
                    break
                res = (res * c)%mod
            for j in range(2*i,mx+1,i):
                res -= cnt[j]
            cnt[i] = res%mod
        return cnt[1]