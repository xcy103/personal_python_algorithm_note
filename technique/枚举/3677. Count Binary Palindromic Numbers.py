#我自己写的，思路还算直观吧
ans = [0]*51
ans[0] = 1
for l in range(1,51):
    ans[l] = pow(2,(l+1)//2-1)
print(ans)
class Solution:
    def countBinaryPalindromes(self,n: int) -> int:
        #从1到n
        #print(len(bin(10**15)[2:]))
        if n==0:return 1
        if n==1:return 2
        high = list(bin(n)[2:])
        t = len(high)
        pre = sum(ans[:t])
    
        path = [1]
        def f(i):
            if i==(t+1)//2:
                if t%2:
                    nums = path[:-1]+path[::-1]
                else:
                    nums = path+path[::-1]
                res = int(''.join(list(map(str,nums))),2)
                if res<=n:
                    return 1
                return 0
            ret = 0
            #发现这一位是1，我们可以选0或者1，如果选0，那么后面可以随便选，所以直接加上后面所有的情况数，如果选1，那么后面只能选和high一样的了
            if high[i]=='1':
                ret+=pow(2,(t-1)//2-i)
            #这个算是一个小技巧，下面表示我们来到最高位置了
            #如果是0，就push0，如果是1，就push1
            path.append(1 if high[i]=='1' else 0)
            ret+=f(i+1)
            return ret
        return pre+f(1)


        