class TimeMap:

    def __init__(self):
        self.binnacle = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.binnacle[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        left, right = 0, len(self.binnacle[key]) - 1

        if len(self.binnacle[key]) < 1 or self.binnacle[key][0][0] > timestamp:
            return ""

        mid = 0

        while left <= right:

            mid = (left + right) // 2

            if self.binnacle[key][mid][0] == timestamp:
                return self.binnacle[key][mid][1]

            elif self.binnacle[key][mid][0] > timestamp:
                right = mid -1

            else:
                left = mid + 1

        return self.binnacle[key][right][1]
        
        
