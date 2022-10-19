def insertionSort(arr):
    for i in range(1,len(arr)):
        itemToInsert = arr[i]
        prev = i - 1

        while prev >=0 and arr[prev] > itemToInsert:
            arr[prev + 1] = arr[prev]
            prev = prev - 1
        arr[prev + 1] = itemToInsert

    print(arr)

insertionSort([1,3,1,343,12,3])
