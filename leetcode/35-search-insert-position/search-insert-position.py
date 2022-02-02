class Solution(object):

    def searchInsert(self, nums, target):

        beg = 0
        end = len(nums)

        while beg < end:
            mid = (beg + end) // 2

            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1

        return beg


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))    # 2
print(solution.searchInsert([1, 3, 5, 6], 2))    # 1
print(solution.searchInsert([1, 3, 5, 6], 7))    # 4
