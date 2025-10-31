# Find the max count of the consecutive same number in a binary array
# Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
# Output: 4
# Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.

# Input: arr[] = [0, 0, 1, 0, 1, 0]
# Output: 2
# Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.

# Input: arr[] = [0, 0, 0, 0]
# Output: 4
# Explanation: The maximum number of consecutive 0’s in the array is 4.

def maxConsecutiveBits(arr):
  count = 1
  maxCount = count
  for i in range(1, len(arr)):
    if arr[i] == arr[i -1]:
      count += 1
    else:
      maxCount = max(count, maxCount)
      count = 1
  return max(maxCount, count)

def maxConsecutiveBitsXor(arr):
  count = 0
  maxCount = 0
  prev = -1 
  for num in arr:
    if (prev ^ num) == 0:
      count += 1
    else:
      maxCount = max(maxCount, count)
      count = 1
    prev = num
  return max(maxCount, count)




if __name__ == '__main__':
  print ('Finding max consecutive number[0/1] in a binary array')
  input_1 = [0, 1, 0, 1, 1, 1, 1]
  input_2 = [0, 0, 1, 0, 1, 0]
  input_3 = [0, 0, 0, 0]

  print ('==============> solution 1')  
  print(maxConsecutiveBits(input_1))
  print(maxConsecutiveBits(input_2))  
  print(maxConsecutiveBits(input_3))

  print ('==============> solution 2')  
  print(maxConsecutiveBitsXor(input_1))
  print(maxConsecutiveBitsXor(input_2))  
  print(maxConsecutiveBitsXor(input_3))  