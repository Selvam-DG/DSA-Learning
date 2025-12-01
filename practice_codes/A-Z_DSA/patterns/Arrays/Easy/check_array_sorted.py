from typing import List

#solution

class Solution:
    def check(self, nums:List[int])->bool:
        for i in range(1, len(nums)):
            # if previous index value is greater than current index value
            if nums[i-1] > nums[i]:
                return False
            
        return True