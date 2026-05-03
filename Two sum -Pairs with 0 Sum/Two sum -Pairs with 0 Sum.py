class Solution:
    def getPairs(self, arr):
        seen = set()
        result = set()
        
        for num in arr:
            if -num in seen:
                pair = tuple(sorted((num, -num)))
                result.add(pair)
            
            seen.add(num)
        
        return sorted(list(result))