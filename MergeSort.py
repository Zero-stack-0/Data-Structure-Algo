def mergeSort(arr):
    if(len(arr)>1):
        midd=len(arr)//2
        left = arr[:midd]
        right = arr[midd:]
        mergeSort(left)
        mergeSort(right)
        
        i=j=k=0
        
        while(len(left)>i and len(right)>j):
            if(left[i]<right[j]):
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
            
        while(len(left)>i):
            arr[k]=left[i]
            i+=1
            k+=1
        while(len(right)>j):
            arr[k]=right[j]
            j+=1
            k+=1
    return(arr)


arr = [54,26,93,17,77,31,44,55,20]
mergeSort(arr)
