class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {v: i for i, v in enumerate(nums)}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in index_map and index_map[complement] != i:
                return sorted([i, index_map[target - n]])