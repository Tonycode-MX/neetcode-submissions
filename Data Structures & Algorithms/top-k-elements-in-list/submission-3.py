class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        top = list(dict(sorted(hashmap.items(), key=lambda item: item[1], reverse= True)).keys())
        print(top)
        return top[0:k]
