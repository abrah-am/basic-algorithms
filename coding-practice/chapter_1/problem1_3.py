def replaceSpaces(str, trueLength):
  char_array = list(str)
  numberOfSpaces = countOfChar(char_array, 0, trueLength, ' ')
  # Base 0 index
  newIndex = trueLength - 1 + numberOfSpaces * 2
  # If there is any excess space add a null char
  if newIndex + 1 < len(char_array):
    char_array[newIndex + 1] = '\0'
  
  for oldIndex in range(trueLength - 1, -1, -1):
    if char_array[oldIndex] == ' ':
      char_array[newIndex] = '0'
      char_array[newIndex - 1] = '2'
      char_array[newIndex - 2] = '%'
      newIndex -= 3
    else:
      char_array[newIndex] = char_array[oldIndex]
      newIndex -= 1  
  
  return ''.join(char_array)

def countOfChar(char_array, start, end, targetChar):
  count = 0
  for i in range(start, end):
    if char_array[i] == targetChar:
      count += 1
  return count

if __name__ == "__main__":
  print('Replace spaces with %20')
  str = "Mr John Smith      "
  # True length does not include trailing spaces
  trueLength = 13
  print(replaceSpaces(str, trueLength))