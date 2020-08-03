class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        _sort = stones
        while len(stones) > 1:
            max1 = max(stones)
            stones.pop(stones.index(max1))
            max2 = max(stones)
            stones.pop(stones.index(max2))
            diff = max1 - max2
            if diff is not 0:
                stones.append(diff)
        
        return stones[0] if len(stones) else 0
