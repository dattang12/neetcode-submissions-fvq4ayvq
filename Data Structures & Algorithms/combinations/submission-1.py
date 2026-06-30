class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(index, path):         
            if (len(path) == k):
                res.append(path[:])
            
            for i in range(index, n+1):
                path.append(i)
                backtracking(i+1, path)
                path.pop()
        
        backtracking(1, [])

        return res
        