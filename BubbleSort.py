# time complexity = O(n2)

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)
bubbleSort([2,6,5,8,3,54])


# comparing element in array if first element is greater than
# other than swap it with nested loop