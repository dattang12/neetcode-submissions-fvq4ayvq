class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(string, open_gate, close_gate):
            if len(string) == 2*n:
                res.append(string)
                return
            
            if open_gate < n:
                backtracking(string + "(", open_gate + 1, close_gate)
            if open_gate > close_gate:
                backtracking(string + ")", open_gate, close_gate + 1)
        
        backtracking("", 0,0)
        
        return res
            
        