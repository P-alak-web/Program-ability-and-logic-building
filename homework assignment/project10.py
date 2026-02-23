def minJumps(arr):
    n = len(arr)
    
    # If array has only one element, no jumps needed
    if n <= 1:
        return 0
    
    # If first element is 0, we can't move anywhere
    if arr[0] == 0:
        return -1
    
    # maxReach stores the maximum index we can reach
    maxReach = arr[0]
    
    # step stores how many steps we can still take
    step = arr[0]
    
    # jump stores the number of jumps made
    jump = 1
    
    for i in range(1, n):
        
        # If we have reached the last index
        if i == n - 1:
            return jump
        
        # Update maxReach
        maxReach = max(maxReach, i + arr[i])
        
        # Use a step to move forward
        step -= 1
        
        # If no more steps remain
        if step == 0:
            jump += 1
            
            # If current index is beyond maxReach, can't move further
            if i >= maxReach:
                return -1
            
            # Re-initialize the steps
            step = maxReach - i
    
    return -1


# Example usage
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr))  # Output: 3