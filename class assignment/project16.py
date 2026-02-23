def common_element(arr1,arr2,arr3):
    i = j = k = 0
    n1,n2,n3 = len(arr1),len(arr2),len(arr3)
    result()
    while i<n1 and j<n2 and k<n3:
        if arr1[i] == arr2[j] == arr3[k]:

          if not result or result[-1]!=arr1[i]:
             result.append(arr1[i])
        else:
           small = min(arr1[i],arr2[i],arr3[i])
           if(arr[i] < small)     
                  
