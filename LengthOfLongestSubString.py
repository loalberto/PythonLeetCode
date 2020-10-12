class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest = 0
        longest_length = []
        temp = []
        for i in range(0, len(s)):
            if s[i] in temp:
                longest_length.append(longest)
                continue
            temp.append(s[i])
            longest += 1
            for j in range(i + 1, len(s)):
                if s[j] in temp:
                    temp = []
                    longest_length.append(longest)
                    longest = 0
                    break
                temp.append(s[j])
                longest += 1
        return max(longest_length)