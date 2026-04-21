class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        """
        题目意思：
        给你两组时间：
        - buses[i]：第 i 辆公交车的发车时间
        - passengers[j]：第 j 个乘客的到达时间
        
        规则：
        1. 乘客如果 arrival <= bus_time 才能上车
        2. 每辆车最多载 capacity 人
        3. 按乘客到达时间从小到大依次上车（先到先上）
        4. 你也要赶车，但：
           ❗ 不能和任何乘客 arrival 时间相同
        
        目标：
        👉 求你“最晚”什么时候到达，还能上某一辆车
        
        
        数据范围：
        - 1 <= len(buses), len(passengers) <= 1e5
        - 1 <= buses[i], passengers[i] <= 1e9
        - buses 所有值互不相同
        - passengers 所有值互不相同
        - capacity <= 1e5
        
        
        核心流程（简述）：
        - 排序 buses 和 passengers
        - 模拟乘客上车（双指针）
        - 只关心最后一辆车：
            - 如果没满 → 可以取 bus 时间
            - 如果满了 → 取最后一个上车的人时间
        - 最后往前跳，避开 passenger 时间
        """

        buses.sort()
        passengers.sort()
        
        i = 0  # passengers 指针
        
        for bus in buses:
            cnt = 0
            while i < len(passengers) and passengers[i] <= bus and cnt < capacity:
                i += 1
                cnt += 1
        
        # 最后一辆车
        if cnt < capacity:
            ans = buses[-1]
        else:
            ans = passengers[i - 1]
        
        # 避免和乘客冲突（不能同一时间）
        s = set(passengers)
        while ans in s:
            ans -= 1
        
        return ans