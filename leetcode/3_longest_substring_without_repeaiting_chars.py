"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = "anviaj"
Output: 5
Explanation: The answer is "jaivn", with the length of 5.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        msg_max = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in msg_max and msg_max[ch] >= left:
                left = msg_max[ch] + 1
            msg_max[ch] = right
            best = max(best, right - left + 1)
        return best

test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb")) # 3
print(test.lengthOfLongestSubstring("bbbbb")) # 1
print(test.lengthOfLongestSubstring("pwwkew")) # 3
print(test.lengthOfLongestSubstring("aab")) # 2
print(test.lengthOfLongestSubstring("dvdf")) # 3
print(test.lengthOfLongestSubstring("anviaj")) # 5

"""
идея классная но костыльная и тест не проходит в обратку
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxTmp = {}
        tmp = {}
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp.update({s[i]: i})
                print(tmp)
                if len(tmp) > len(maxTmp):
                    maxTmp.clear()
                    maxTmp.update(tmp)
            elif s[i] in tmp:
                if s[i-1] != s[i]:
                    del tmp[s[i-2]]
                    tmp.update({s[i]: i})
                else:
                    tmp.clear()
                    tmp.update({s[i]: i})
        return len(maxTmp.keys())
"""