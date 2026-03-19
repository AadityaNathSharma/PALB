class Solution:    
    def findUnion(self, a, b):
        result = set(a)   # add all elements of a
        
        for num in b:
            result.add(num)
        
        return list(result)
