class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letters = ["","",'abc','def' ,'ghi','jkl',
                         'mno','pqrs','tuv','wxyz']

        ans = [""]

        for d in digits:
            new = []
            for comb in ans:
                for letter in letters[int(d)]:
                    new.append(comb + letter)
            ans = new

        return ans
