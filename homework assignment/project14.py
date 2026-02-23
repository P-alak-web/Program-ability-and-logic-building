def combinationSum2(candidates, target):
    candidates.sort()  # Sort to handle duplicates
    result = []

    def backtrack(start, current_combination, remaining_target):
        # If remaining target becomes 0, we found a valid combination
        if remaining_target == 0:
            result.append(current_combination[:])
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicate elements at the same recursion level
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # If current number is greater than remaining target, stop
            if candidates[i] > remaining_target:
                break
            
            # Choose the current number
            current_combination.append(candidates[i])
            
            # Move to next index (i + 1) because each number can be used once
            backtrack(i + 1, current_combination, remaining_target - candidates[i])
            
            # Backtrack (remove last added number)
            current_combination.pop()

    backtrack(0, [], target)
    return result


# ------------------------
# Example 1
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
print("Example 1 Output:")
print(combinationSum2(candidates1, target1))

# ------------------------
# Example 2
candidates2 = [2, 5, 2, 1, 2]
target2 = 5
print("\nExample 2 Output:")
print(combinationSum2(candidates2, target2))