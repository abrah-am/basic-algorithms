def getSecondLargestOption1(arr):
    size = len(arr)
    arr.sort()

    for i in range(size - 2, -1, -1):
        if arr[i] != arr[i + 1]:
            return arr[i]
        
    return -1

def getSecondLargestOption2(arr):
    n = len(arr)
    secondLargest = -1
    largest = -1 

    for i in range(n):
      if arr[i] > largest:
          largest = arr[i]
    
    for i in range(n):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest

def getSecondLargestOption3(arr):
    n = len(arr)

    secondLargest = -1
    largest = -1

    for i in range(n):
        if arr[i] > largest:
          secondLargest = largest
          largest = arr[i]

        elif  arr[i] > secondLargest and arr[i] != largest:
          secondLargest = arr[i]
    
    return secondLargest

if __name__ == '__main__':
    arr = [12, 35, 1, 10, 34, 1]
    arr2 = [12, 35, 35, 10, 34, 1]
    arr3 = [35, 35, 35, 35, 35, 35]

    print(getSecondLargestOption1(arr))    
    print(getSecondLargestOption1(arr2))    
    print(getSecondLargestOption1(arr3))    
    
    print(getSecondLargestOption2(arr))
    print(getSecondLargestOption2(arr2))
    print(getSecondLargestOption2(arr3))
    
    print(getSecondLargestOption3(arr))    
    print(getSecondLargestOption3(arr2))
    print(getSecondLargestOption3(arr3))        