class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1 - find intersection
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]   
            if slow == fast:
                break
        
        # phase 2 - find entrance to cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        