# Neetcode 150 - completed by Joseph Jatou

# 1/150 - Contains Duplicates

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:       
        seen = set() # Sets contain no duplicates

        for i in nums: # I-Trade through nums array
            if i in seen:    # If the current number is located in the non-duplicate data structure...
                return True   #  return True meaning there are duplicates (having a number in the i trading that is already in the seen set)
            seen.add(i)  # use the .add() module from built in python sets to add to the seen

        return False # return False if the condition of duplicates have not been met.
    
    