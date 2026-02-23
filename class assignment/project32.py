#combinational sum

def combinationalsum(arr,target):
    result = []

    def dfs(index,remaining,path):
        
        #if target became zero = valid combination
        if remaining == 0:
            result.append(path[:])
            return
        
        # if out of bond
        if index >= len(arr) or remaining < 0:
            return
        
        # include index into path
        path.append(arr[index])
        dfs(index, remaining-arr[index],path)
        path.pop()

        #exclude the index into path
        dfs(index+1, remaining, path)

    dfs(0,target,[])
    return result

arr = [2,3,5]
target = 8
print(f"output : {combinationalsum(arr,target)}")    