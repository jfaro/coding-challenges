class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = []
        max_subarray_sum = float('-inf')

        # Init array
        for i in range(0, len(nums)):
            row = []
            for j in range(0, len(nums)):
                row.append('X')
            dp.append(row)

        # DP
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):

                # Base case (subarray of length 1)
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j - 1] + nums[j]

                if dp[i][j] > max_subarray_sum:
                    max_subarray_sum = dp[i][j]

        return max_subarray_sum


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6
print(solution.maxSubArray([1]))                                # 1
print(solution.maxSubArray([5, 4, -1, 7, 8]))                   # 23
