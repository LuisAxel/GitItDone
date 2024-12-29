class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for number in arr:
            count[number] += 1

        ocurrences = set()
        for key in count.keys():
            if count[key] in ocurrences:
                return False
            ocurrences.add(count[key])

        return True
