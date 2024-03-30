class Solution:
    def lastStoneWeight(self, stones:int) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()  # Remove the heaviest stone
            x = stones.pop()  # Remove the second heaviest stone
            if x != y:
                stones.append(y - x)  # Smash the stones together and add the remaining weight
        return stones[0] if stones else 0  # Return the weight of the last remaining stone, or 0 if there are no stones left