class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        global_max_sum = nums[0]
        current_max_sum = nums[0]

        for i in range(1, len(nums)):
            current_max_sum = max(current_max_sum + nums[i], nums[i])
            global_max_sum = max(global_max_sum, current_max_sum)

        return global_max_sum


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6
print(solution.maxSubArray([1]))                                # 1
print(solution.maxSubArray([5, 4, -1, 7, 8]))                   # 23
print(solution.maxSubArray([-57, 9, -72, -72, -62, 45, -97, 24, -39, 35, -
                            82, -4, -63, 1, -93, 42, 44, 1, -75, -25, -87, -16, 9, -59, 20, 5, -95]))
