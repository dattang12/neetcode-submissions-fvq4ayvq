class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_nums = 0
        j = 0
        min_l = float('inf')
        

        for i in range(len(nums)):
            sum_nums += nums[i]
            
            while sum_nums >= target:
                min_l = min(min_l, i - j + 1)
                sum_nums -= nums[j]
                j += 1
        
        return 0 if min_l == float('inf') else min_l
                    
                


            
        