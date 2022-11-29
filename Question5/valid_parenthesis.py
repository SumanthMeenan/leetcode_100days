class Solution:
    
    def isValid(self, s: str) -> bool:
        data = {"{}","[]","()"}
        if len(s)%2 != 0:
            return False
        while any(elem in s for elem in data):
            for elem in data:
                s = s.replace(elem,"")
        if len(s):
            return False
        else:
            return True


if __name__ == "__main__":
    s = input("Enter a string of parenthesis: ")
    print(Solution().isValid(s))