class Solution:    
    def findUnion(self, a, b):
        result = set()
        
        for num in a:
            result.add(num)
        
        for num in b:
            result.add(num)
        
        return list(result)
