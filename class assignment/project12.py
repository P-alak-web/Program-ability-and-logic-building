def minimum_height(arr,k):

    #sort the array
    arr.sort()  

    #initial differnce
    n = len(arr)
    result = arr[n-1] - arr[0]
    
    #increase or decrease the hieght of tower by 1
    small = arr[0] + k
    big = arr[-1] - k

    # we are avoiding small >= big
    if small > big:
        small, big = big,small
    for i in range(1,n):
        subtract = arr[i] - k
        add = arr[i] + k

        if subtract < 0 :
            continue
        new_min = min(small,subtract)
        new_max = max(big,add) 

        result = min(result, new_max - new_min)
arr = [3,9,12,16,20]
k=3

print(f"output:{minimum_height(arr,k)}")       