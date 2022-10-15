# Program To demonstrate of Insertion Sort

def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
num=int(input("Enter the length of the array"))
arr=[]
for data in range(1,num):
  arr.append(int(input("Enter the number:")))
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])


