class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # edge cases
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 1
        max_reach = arr[0]
        steps = arr[0]
        
        for i in range(1, n):
            # reached end
            if i == n - 1:
                return jumps
            
            max_reach = max(max_reach, i + arr[i])
            steps -= 1
            
            # no steps left → must jump
            if steps == 0:
                jumps += 1
                
                # can't move further
                if i >= max_reach:
                    return -1
                
                steps = max_reach - i
        
        return -1
