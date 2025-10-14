from typing import List

class Solution:
    def rotateLeftByOne(self, nums:List[int])->None:
        # store the first element in temp variable
        # shift the element by one position before
        n = len(nums)
        temp = nums[0]
        for i in range(n-1):
            nums[i] = nums[i+1]
        nums[-1] = temp
        
    def rotateRightByOne(self, nums:List[int])->None:
        #store the last element in temp
        # shift the each element by one positio ahead
        n = len(nums)
        temp = nums[-1]
        for i in range(n-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp
        
    def rotateLeftByk(self, nums:List[int], k:int) -> None:
        n = len(nums)
        if n == 0 or k%n == 0:
            return
        k = k % n
        temp = nums[:k]
        
        for i in range(n-k):
            nums[i] = nums[k+i]
        nums[n-k:] = temp
    
    def rotateRightByk(self, nums:List[int], k:int) -> None:
        n = len(nums)
        if n == 0 or k%n == 0:
            return
        k = k % n
        temp = nums[-k:] 
        for i in range(n-1, k-1, -1):
            nums[i] = nums[i-k]
        
        for i in range(len(temp)):
            nums[i] = temp[i]
    
    def rotateLeftByKOptimal(self, nums:List[int], k:int) -> None:
        n = len(nums)
        if n==0 or k%n==0:
            return
        k = k % n
        self.reverseList(nums, 0, k-1)
        self.reverseList(nums, k, n-1)
        self.reverseList(nums, 0 ,n-1)
        
    def reverseList(self, nums:List[int],left:int, right:int) ->None:
        
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        print(nums)
        

if __name__=="__main__":
    nums = [1,2,3,4,5,6, 7]
    k = 3
    sol = Solution()
    sol.rotateLeftByKOptimal(nums, k)
    print(nums)
    
        
        
        