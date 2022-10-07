from random import sample
from typing import List


def mergeSort(array: List) -> List:
    # the first element of the list is assumed to be sorted
    # starting with the second element
    for i in range(1, len(array)): 
        key = array[i]
        prev = i - 1
        # comparing every element with the key and placing it in the right position
        while prev >= 0and key < array[prev]: 
            array[prev + 1] = array[prev]
            prev -= 1
        array[prev + 1] = key
    return array


if __name__ == "__main__":
    # creating random test cases
    for _ in range(10):
        test_case = sample(range(1, 100), 7)
        print("testing with: ", test_case)
        print("result: ", mergeSort(test_case))

