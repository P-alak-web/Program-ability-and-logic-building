# binary search : return the index of the target v
# 2 pointer index
def searchindex(arr,target):
    left = 0
    right = len(arr)-1

    while left <= right :
        mid = (left + right)//2

        #if element exist in the array
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid +1

        else:
            right = mid - 1

        #if element is not found
    return left

arr = [1,3,5,7]
print(f"output:{searchindex(arr,2)}")         
