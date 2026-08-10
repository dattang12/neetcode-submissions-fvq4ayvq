class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(index, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or index == len(nums):
                return
            
            #include nums[i]
            path.append(nums[index])
            backtracking(index+1,path,total+nums[index])
            path.pop()

            #skip nums[i]

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index+=1
            backtracking(index+1,path,total)
        backtracking(0,[],0)
        return res



