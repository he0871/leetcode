class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left  = nums[:mid]
        right = nums[mid:]
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        i = 0
        j = 0
        while i < len(left) or j < len(right):
            if i >= len(left):
                nums[i+j] = right[j]
                j += 1
                continue
            elif j >= len(right):
                nums[i+j] = left[i]
                i += 1
                continue
            elif left[i] < right[j]:
                nums[i+j] = left[i]
                i += 1
            elif left[i] >= right[j]:
                nums[i+j] = right[j]
                j += 1
           
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
