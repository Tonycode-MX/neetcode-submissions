class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        days = []
        
        for day in range(n):
            if not days:
                days.append(day)
            else:
                
                while days and temperatures[day] > temperatures[days[-1]]:
                    last_day = days.pop()
                    res[last_day] = day - last_day
                days.append(day)

        return res