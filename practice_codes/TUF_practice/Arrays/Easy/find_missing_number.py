from typing import List

class Solution:
    
    def findMissingNum(self, nums:List[int])->int:
        #Brute Force - Time complexity = O(n²)
        n = len(nums)
        
        for i in range(n):
            flag = 0
            for num in nums:
                if num == i:
                    flag = 1
                    break
            if flag == 0:
                return i 
        return n
    
    def findMissingNum2(self, nums:List[int])->int:
        # Better approach - O(2n)
        # hash map
        n = len(nums)
        unique_nums = dict()
        for num in nums:
            unique_nums[num]  = 1 
        for i in range(n+1):
            if i not in unique_nums:
                return i
            
        return n
    
    def findMissingNum3(self, nums:List[int])-> int:
        n = len(n)
        total_sum = n *(n+1)/2
        sum = 0
        for num in nums:
            sum += num
            
        return abs(total_sum-sum)
    

if __name__=="__main__":
    nums = [0,1,3,2,4,6]
    sol = Solution()
    missing_num = sol.findMissingNum2(nums)
    print("Missing Number: ", missing_num)