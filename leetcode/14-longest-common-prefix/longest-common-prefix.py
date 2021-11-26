class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if not strs:
            return ""

        shortest_str = min(strs, key=len)

        for i, c in enumerate(shortest_str):
            for str in strs:
                if str[i] != c:
                    return shortest_str[:i]

        return shortest_str


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
