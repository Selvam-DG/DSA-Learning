from typing import List

# Union and Intersection of two Sorted Arrays
class Solution:
    
    def unionSorted(self, nums1:List[int], nums2:List[int])->List[int]:
        result = set()
        
        for num in nums1:
            if num not in result:
                result.add(num)
        
        for num in nums2:
            if num not in result:
                result.add(num)
            
        return list(result)
    
    def uninonSortedOptimal(self, nums1:List[int], nums2:List[int])->List[int]:
        res = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                if len(res) == 0 or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                if len(res) == 0 or nums2[j] != res[-1] :
                    res.append(nums2[j])
                j += 1
        n3 = len(res)
        while i < n1:
            if len(res) == 0 or nums1[i] != res[-1]:
                res.append(nums1[i])
            i+=1
        while j < n2:
            if len(res) == 0 or nums2[j]!= res[-1]:
                res.append(nums2[j])
            j+=1
        return res
    
    def intersectSorted(self, nums1:List[int], nums2:List[int])->List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        
        dummy = [0]*n2
        
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 < num2:
                    break
                if num1 == num2 and dummy[j] == 0:
                    res.append(num1)
                    dummy[j] = 1
                    break
            
        return res
    
    def intersectSortedOptimal(self, nums1:List[int], nums2:List[int])->List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        i = j = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
            
                
    
if __name__=="__main__":
    nums1 = [1,2,3,3,4,5,5]
    nums2 = [2,3, 4, 5,5,6,7]
    
    sol = Solution()
    
    union = sol.intersectSortedOptimal(nums1, nums2)
    
    print(union)