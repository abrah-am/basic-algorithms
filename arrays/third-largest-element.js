function thirdLargestElement(arr) {
  let n = arr.length

  let first = -Infinity, second = -Infinity, third = -Infinity

  for (let i = 0; i < n; i++) {

    if (arr[i] > first) {
      third = second
      second = first
      first = arr[i]
    }

    else if (arr[i] > second) {
      third = second
      second = arr[i]
    }

    else if (arr[i] > third) {
      third = arr[i]
    }
  }
  return third
}



let arr = [1, 14, 2, 16, 10, 20];
console.log(thirdLargestElement(arr))