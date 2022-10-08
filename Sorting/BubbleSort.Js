let arr = [8, 5, 6, 4, 7, 9, 1, 3, 2, 10]


function swap(array, x, y) {
    let temp = array[x];
    array[x] = array[y];
    array[y] = temp;
}


function sorter(array, n) {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(array, j, j + 1)
            }
        }
    }
}

sorter(arr, 10)
function printArray(array, n) {
    for (i = 0; i < n; i++) {
        document.write(array[i] + " ");
        document.write("\n");
    }
}
printArray(arr, 10)