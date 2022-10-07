# Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for _ in range(n):

        for j in range(n - 1):

            if arr[j] > arr[j + 1]:

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


res = bubbleSort([55, 33, 2232, 545, 24, 3, 243, 223, 1, 445])

print(res)
