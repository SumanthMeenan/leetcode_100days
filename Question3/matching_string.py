from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str, max_str = min(strs), max(strs)
        for index, val in enumerate(min_str):
            print(index, val)
            if val != max_str[index]:
                return min_str[:index]
        return min_str 

     
if __name__ == "__main__":
    strs = input("Input List of strings: ")
    print(Solution().longestCommonPrefix(strs))