function secondLargestElementOption1(arr) {
  arr.sort((a, b) => a - b)
  
  for (let i = arr.length - 2; i >= 0; i--) { 
    if(arr[i] !== arr[i+1]) {
      return arr[i]
    }
  }
  return -1
}

function secondLargestElementOption2(arr) {
  let largest = -1,
    secondLargest = -1;

  // Find the largest element
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  // Find the second largest element
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > secondLargest && arr[i] != largest) {
      secondLargest = arr[i];
    }
  }

  return secondLargest;
  
}

function secondLargestElementOption3(arr) { 
  let secondLargest = -1, largest = -1

  for (let i = 0; i < arr.length; i++) { 
    if (arr[i] > largest) {
      secondLargest = largest
      largest = arr[i]
    }
    else if (arr[i] < largest && arr[i] > secondLargest){
      secondLargest = arr[i]
    }
  }
  return secondLargest
}

const arr = [12, 35, 1, 10, 34, 1]
const arr2 = [12, 35, 35, 10, 34, 1]
const arr3 = [35, 35, 35, 35, 35, 35];

console.log("Second largest element option 1 is", secondLargestElementOption1(arr))
console.log("Second largest element option 1 is", secondLargestElementOption1(arr2))
console.log("Second largest element option 1 is", secondLargestElementOption1(arr3))

console.log("Second largest element option 2 is", secondLargestElementOption2(arr))
console.log("Second largest element option 2 is", secondLargestElementOption2(arr2))
console.log("Second largest element option 2 is", secondLargestElementOption2 (arr3))

console.log("Second largest element option 3 is", secondLargestElementOption3(arr))
console.log("Second largest element option 3 is", secondLargestElementOption3(arr2))
console.log("Second largest element option 3 is", secondLargestElementOption3(arr3))