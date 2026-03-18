#你要明白题目的收益，是上的课的数量，你的代价就是上课的时间
#先按照结束时间从小到大排序，如果当前时间加上上课时间
#小于课程截止时间，则加入，把你付出的代价放入最大堆
#如果发现，你要上的课的时间，加上当前时间，超过了截止时间，
#你需要看看堆顶的的课，付出的代价是否小于当前课程的代价，
#如果小于，那就继续，不上当前这门课，如果大于，说明我还不如不上之前
#这个代价大的课，弹出堆，选我们代价小的课去上，同时调整当前时间
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        h = []
        times = 0
        for d,e in courses:
            if times + d<=e:
                times+=d
                heappush(h,-d)
            elif h and -h[0]>d:
                times += d+heappop(h)
                heappush(h,-d)
        return len(h)