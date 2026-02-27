from typing import List

# --- PASTE THIS PART INTO LEETCODE ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i
        return []
# -------------------------------------

# --- RUN THIS LOCALLY  ---
if __name__ == '__main__':
    sol = Solution()
    
    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Output: {sol.twoSum(nums, target)}")