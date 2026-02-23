def twoSum(nums, target):
    num_map = {}  # Dictionary to store number and its index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in dictionary
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store the current number with its index
        num_map[num] = i

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)