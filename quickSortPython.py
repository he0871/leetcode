class Solution:
    def partition(self, nums, lo, hi):
        
        i,j = lo, hi
        pivot = nums[hi]
        while i < j:
            while i < j and nums[i] < pivot:
                i += 1
            while i < j and nums[j] >= pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[hi] = nums[hi], nums[i]
        return i
                
            
            
    def quickSort(self, nums, lo, hi):
        if lo >= hi:
            return nums
        k = self.partition(nums, lo, hi)
        self.quickSort(nums, lo, k-1)
        self.quickSort(nums, k+1, hi)
        return nums
        
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums)-1)
