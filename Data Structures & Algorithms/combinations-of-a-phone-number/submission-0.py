class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtracking(index, string):
            # string is now "full" — matches length of digits
            if len(string) == len(digits):
                res.append(string)
                return
            
            next_digit = digits[index]        # the digit we're working on now
            for letter in phone_map[next_digit]:
                backtracking(index + 1, string + letter)  # add one letter, move to next digit

        backtracking(0, "")
        return res