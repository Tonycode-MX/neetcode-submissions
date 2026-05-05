class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        hashmap = {}

        for element in nums:
            hashmap[element] = hashmap.get(element,0) + 1

        res = 1

        for num in hashmap:
            if num - 1 not in hashmap:
                i, count = 1, 1
                next = True
                while next:
                    if num + i in hashmap:
                        count+=1
                    else:
                        next = False
                    i+=1
                if count > res:
                    res = count
        return res



        