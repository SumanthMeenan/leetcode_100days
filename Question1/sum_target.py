from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for elem in nums:
            c = target/2
            if nums.count(c) >1:
                a = nums.index(c)
                b = a+1+nums[a+1:].index(c)
                return [a, b]
            elif target-elem in nums and c != elem:
                return [nums.index(elem), nums.index(target - elem)]     

if __name__ == "__main__":
    nums = list(map(int, input("Enter a list of integers: ").split()))
    target = int(input("Enter a target value: "))
    print(Solution().twoSum(nums, target))
