let array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
function search(arr, element) {
    for (let index = 0; index < arr.length; i++) {
        if (arr[index] == element) {
            return true;
        }
    }
    return false;
}