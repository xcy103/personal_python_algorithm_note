import heapq
def isPossible(target):
    n = len(target)
    s = sum(target)
    h = []
    for x in target:
        heapq.heappush(h,-x)
    
    while 1:
        cur = heapq.heappop(h)
        if cur==-1:break
        cur = -cur
        if cur<=s-cur: return False
        other = s - cur
        cur = cur%other
        s = cur + other
        heapq.heappush(h,-cur)
    
    return True
isPossible([8,5])