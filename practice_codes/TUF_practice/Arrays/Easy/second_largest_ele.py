from typing import List

class Solution:
    def secondLargest(self, nums:List[int]) -> int:
        
        # # ---------- BRUTE FORECE ----------
        # # sor the array in non descending
        # # return the second largest element by comparing with the largest element
        # n = len(nums)
        # nums.sort()
        # largest = nums[-1]
        # for i in range(n-2, -1, -1 ):
        #     if nums[n-2] < largest:
        #         return nums[n-2]
        # return -1
        
        
        # # -------------- Better Solution
        # # find the largest element
        # # compare the elements with largest element and find the second largest
        # n = len(nums)
        # largest = nums[0]
        # for i in range(1, n):
        #     if nums[i] > largest:
        #         largest = nums[i]
        
        # second_largest = -1
        # for i in range(n):
        #     if nums[i] > second_largest and nums[i] != largest:
        #         second_largest = nums[i]
        # return second_largest
        
        # -------- Optimal --------------
        # initally start with largest and secondlargest element
        # loop through the array and if element is greater than the largest, swap the element to largest and largest element to second largest
        
        largest = nums[0]
        second_largest = float('-inf')
        
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return second_largest
                
        
if __name__=="__main__":
    sol = Solution()
    test_case = int(input("Enter number of test cases: "))
    
    for i in range(test_case):
        nums = list(map(int, input(f"Enter numbers seperated by spaces for the test case {i+1}: ").split()))
        if len(nums) >= 2:
            print("Second largest Element: ", sol.secondLargest(nums))
        else:
            print("Minimum 2 element required in array")