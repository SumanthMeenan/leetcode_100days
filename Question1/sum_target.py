from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for elem in nums:
            if nums.count(target/2) >1:
                a = nums.index(target/2)
                b = a+1+nums[a+1:].index(target/2)
                return [a, b]
            elif target-elem in nums and target/2 != elem:
                return [nums.index(elem), nums.index(target - elem)]     

if __name__ == "__main__":
    nums = list(map(int, input("Enter a list of integers: ").split()))
    target = int(input("Enter a target value: "))
    print(Solution().twoSum(nums, target))
