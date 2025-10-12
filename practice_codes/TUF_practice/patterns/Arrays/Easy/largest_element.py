from typing import List

class solution:
    def largestElement(self, nums:List[int]) -> int:
        
        # # ---------- Brute Force ----------
        # nums.sort()
        # return nums[-1]
        
        # ------------ Optimal -----------
        if not nums:
            return -1
        largest = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > largest:
                largest = nums[i]
        return largest
                
            
    
    

if __name__ == '__main__':
    test_case = int(input("Enter number of test cases: "))
    sol = solution()
    
    for i in range(test_case):
        nums = list(map(int, input(f"Enter numbers seperated by spaces for test cases {i+1}: ").split()))
        print("Largest Element: ", sol.largestElement(nums))