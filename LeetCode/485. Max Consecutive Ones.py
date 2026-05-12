class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_v=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                max_v=max(count,max_v)
            else:
                count=0
        return max_v

        