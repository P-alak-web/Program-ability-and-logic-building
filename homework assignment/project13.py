def combinationSum2(candidates, target):
    candidates.sort()  # Sort to handle duplicates
    result = []
    
    def backtrack(start, path, remaining):
        # If target becomes 0, we found a valid combination
        if remaining == 0:
            result.append(path[:])
            return
        
        # If remaining becomes negative, stop exploring
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates at the same recursion level
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # Stop if current number exceeds remaining target
            if candidates[i] > remaining:
                break
            
            # Choose the current number
            path.append(candidates[i])
            
            # Recurse with next index (each number used once)
            backtrack(i + 1, path, remaining - candidates[i])
            
            # Backtrack
            path.pop()
    
    backtrack(0, [], target)
    return result


# -------------------------
# Example 1
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
print("Example 1 Output:")
print(combinationSum2(candidates1, target1))

# -------------------------
# Example 2
candidates2 = [2, 5, 2, 1, 2]
target2 = 5
print("\nExample 2 Output:")
print(combinationSum2(candidates2, target2))