class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        sort = ""
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in d:
                d[sort] = [i]
            else:
                d[sort].append(i)
        return d.values()
