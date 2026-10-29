class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(enumerate(nums.copy()), key=lambda e: e[1])
        i = 0
        j = len(nums2) - 1
        while i != j:
            sum = nums2[i][1] + nums2[j][1]
            if sum == target:
                return sorted([nums2[i][0], nums2[j][0]])
            elif sum < target:
                i += 1
            elif sum > target:
                j -= 1
