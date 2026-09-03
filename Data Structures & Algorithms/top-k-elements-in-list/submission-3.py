class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        res = []

        while k > 0:
            top = max(seen, key=seen.get)  # key with the highest count
            res.append(top)
            del seen[top]
            k -= 1

        return res