class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        s_len = len(s)
        word_len = len(words[0])
        n_words = len(words)
        concat_len = word_len * n_words

        word_dict = {}
        for i in words:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1

        seen = {}
        count = 0
        ans = []
        l = 0

        # Window_size = concat_len
        while l < s_len - concat_len + 1:
            seen = {}
            count = 0
            r = l
            # Test for concat_string
            while r < l + concat_len:
                test = s[r:r+word_len]
                r += word_len
                if test not in word_dict:
                    break

                if test in seen:
                    seen[test] += 1
                else:
                    seen[test] = 1

                if seen[test] > word_dict[test]:
                    break
                count += 1

            if count == n_words:
                ans.append(l)
            l += 1
        return ans
