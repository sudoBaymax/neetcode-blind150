# Neetcode 150 - completed by Joseph Jatou

# 2/150 - Longest Substring Without Repeating Characters

class Solution:
    # 1) USE SLIDING WINDOW ALGORITHM (2 pointers)
    #         # 2) USE A SET TO STORE UNIQUE CHARACTERS
    #         # 3) MOVE RIGHT POINTER AND ADD CHAR TO SET
    #         # 4) IF CHAR IN SET, MOVE LEFT POINTER AND REMOVE CHAR FROM SET
    #         # 5) UPDATE MAX LENGTH IF CURRENT LENGTH IS GREATER

    #         # Program Details

    #             # Expand (eg. increase front pointer +1) if ALL CHARACTERS in substring are unique
    #             # Shrink (eg. increase rear pointer +1) if a duplicate is found

    #         # Things we know

    #             # We need some sort of variable that tracks duplicate characters (eg. Sets or Tuples)
    #             # We need 2 variables for the pointer locations
    #             # Once there is a duplicate, mark down the length of the substring, and mover rear pointer +1
    #             # We might need a list of all the substring lengths withought duplicates

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()   
        rear = 0
        max_length = 0

        for front in range(len(s)):
            while s[front] in char_set:
                char_set.remove(s[rear])
                rear += 1
            
            char_set.add(s[front])
            max_length = max(max_length, front - rear + 1)

        return max_length

x = Solution()

print(x.lengthOfLongestSubstring('zxyzxyz'))
print(x.lengthOfLongestSubstring('xxxx'))