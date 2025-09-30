# Reverse the array
# Input: arr[] = [1, 4, 3, 2, 6, 5]  
# Output:  [5, 6, 2, 3, 4, 1]

# Naive approach
# Time Complexity: O(n) 
# Auxiliary space: O(n)
def naive(arr):
  n = len(arr)
  temp_arr = [0] * n
  for i in range(n):
    temp_arr[i] = arr[n - i - 1]
  for i in range(n):
    arr[i] = temp_arr[i]  

# Expected approach 1 - Two pointers
def two_pointers(arr):
  n = len(arr)
  left = 0 
  right = n - 1

  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Expected approach 2 - Swapping Positions
# Time Complexity: O(n), the loop runs through half of the array, so it's linear with respect to the array size.
# Auxiliary Space: O(1), no extra space is required, therefore we are reversing the array in-place.
def swapping_array(arr):
  n = len(arr)

  for i in range(n//2):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]


if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6]  
  print("originalArray:", arr)
  naive(arr)
  print("reversed-naive: ", arr)

  arr = [1, 2, 3, 4, 5, 6]  
  print("originalArray:", arr)
  two_pointers(arr)
  print("reversed-two-pointers: ", arr)

  arr = [1, 2, 3, 4, 5, 6]  
  print("originalArray:", arr)
  swapping_array(arr)
  print("reversed-swapped: ", arr)

  arr = [1, 2, 3, 4, 5, 6]  
  print("originalArray:", arr)
  arr.reverse()
  print("reversed-builtIn: ", arr)