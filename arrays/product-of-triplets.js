/**
 * Find the maximum product of triplets:
 * In an array multiply three items and find what is the maximum product in the array.
 *
 * Examples:
 * arr[] = [10, 3, 5, 6, 20]
 * max product = 10 * 6 * 20 = 1200
 *
 * arr[] = [-10, -3, -5, -6, -20]
 * max product = -3 * -5 * -6 = -90
 *
 * arr[] = [1, -4, 3, -6, 7, 0]
 * max product = -6 * -4 * 7 = 168
 *
 */

// Naive Approach: Use nested loops to find the maximum product
function naiveApproach(arr) {
  let maxProduct = -1e9;

  for (let i = 0; i < arr.length - 2; i++) {
    for (let j = i + 1; j < arr.length - 1; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        maxProduct = Math.max(maxProduct, arr[i] * arr[j] * arr[k]);
      }
    }
  }

  return maxProduct;
}

// Better Approach:
// - Sort in ascending order. If there are negative numbers, they will be the first ones and the positive will be the last
// - return the max product of:  the first two elements (if negative, it will be positive) and the last element or the product of the last three elements, the major ones.
function betterApproach(arr) {
  let maxProduct = -1e9;
  let n = arr.length;

  arr.sort((a, b) => a - b);

  // return max between elements (first * second * last) and (last three elements)
  return Math.max(
    arr[0] * arr[1] * arr[n - 1],
    arr[n - 1] * arr[n - 2] * arr[n - 3]
  );
}

// Expected approach
// This approach will find the three largest items in the array without sorting and the two smallest elements (if negative will be positive) and then find the max between those two.
// Similar approach to the betterApproach but without sorting. Eliminates sorting time.
function expectedApproach(arr) {
  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;
  let thirdLargest = Number.MIN_SAFE_INTEGER;

  let smallest = Number.MAX_SAFE_INTEGER;
  let secondSmallest = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
      thirdLargest = secondLargest;
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] > secondLargest) {
      thirdLargest = secondLargest;
      secondLargest = arr[i];
    } else if (arr[i] > thirdLargest) {
      thirdLargest = arr[i];
    }

    if (arr[i] < smallest) {
      secondSmallest = smallest;
      smallest = arr[i];
    } else if (arr[i] < secondSmallest) {
      secondSmallest = arr[i];
    }
  }
  return Math.max(
    largest * secondLargest * thirdLargest,
    smallest * secondSmallest * largest
  );
}

arr = [10, 3, 5, 6, 20];
arr2 = [-10, -3, -5, -6, -20];
arr3 = [1, -4, 3, -6, 7, 0];

console.log(
  "NaiveApproach: arr =",
  naiveApproach(arr),
  "; arr2 =",
  naiveApproach(arr2),
  "; arr3 =",
  naiveApproach(arr3)
);
console.log(
  "betterApproach: arr =",
  betterApproach(arr),
  "; arr2 =",
  betterApproach(arr2),
  "; arr3 =",
  betterApproach(arr3)
);
console.log(
  "expectedApproach: arr =",
  expectedApproach(arr),
  "; arr2 =",
  expectedApproach(arr2),
  "; arr3 =",
  expectedApproach(arr3)
);
