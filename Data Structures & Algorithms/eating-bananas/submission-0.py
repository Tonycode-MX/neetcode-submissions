class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        best_speed = right

        while left <= right:
            k = (left + right) // 2

            hour_count = 0

            for pile in piles:
                hour_count += -(-pile // k)

            if hour_count <= h:
                best_speed = k

                right = k-1

            else:
                left = k+1

        return best_speed





        




        