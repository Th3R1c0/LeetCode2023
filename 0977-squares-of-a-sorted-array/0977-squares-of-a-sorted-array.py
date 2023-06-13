class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        
        while l <= r: 
            if abs(nums[l]) > abs(nums[r]): 
                sqrd = abs(nums[l]) ** 2
                res.append(sqrd)
                l += 1
            else: 
                sqrd = abs(nums[r]) ** 2
                res.append(sqrd)
                r -= 1
                
        return res[::-1]