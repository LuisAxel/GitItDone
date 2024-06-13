class Solution:
    def minWindow(self, s: str, t: str) -> str:

        len_s, n_c = len(s), len(t)

        ans = ""
        t_dict = defaultdict(int)

        for i in t:
            t_dict[i] += 1

        l, r = 0, 0
        count = 0

        #Increment window size until t is found
        while r < len_s:
            if t_dict[s[r]] > 0:
                count += 1
            t_dict[s[r]] -= 1
            r += 1

            #Once found, reduce from left until t is lost
            while count == n_c:
                if r - l < len(ans) or ans == "":
                    ans = s[l:r]

                if t_dict[s[l]] == 0:
                    count -= 1
                t_dict[s[l]] += 1
                l += 1

        return ans
