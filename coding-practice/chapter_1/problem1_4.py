# Check if a string (ignoring casing and non-letters) is a permutation of a palindrome.
# If there is an upper case letter, it has to be counted as lower case
# Example 1: 
#  Input: "Tact Coa"
#  Output: True (Permutations: 'taco cat', 'atco cta', etc)
# Example 2:
#  Input: "it is raining"
#  Output: False

# Solution1: This algorith takes O(N) time where N is the length of the string
def isPermutationOfPalindromeSolution1(phrase: str) -> bool:
  print('isPermutationOfPalindrome > Input: ' + phrase)
  frequencyTable = buildFrequencyTable(phrase)
  return hasOneOddMaxCount(frequencyTable)
  return False

def hasOneOddMaxCount(frequencyTable: list) -> bool:
  oddFound = False
  for count in frequencyTable:
    if count % 2 == 1:
      if oddFound:
        return False # More than one odd count for a character was found.
      oddFound = True
  return True

def getCharIndex(character: chr) -> int:
  intA = ord('a')
  intZ = ord('z')
  intChar = ord(character.lower())
  if intChar >= intA and intChar <= intZ: 
    return intChar - intA
  return -1

def buildFrequencyTable(phrase: str) -> list:
  frequencyTable = [0] * (ord('z') - ord('a') + 1)
  for char in phrase:
    index = getCharIndex(char)
    if index != -1:
      frequencyTable[index] += 1  # Convert to lowercase for case-insensitive comparison
  return frequencyTable

# Solution 2: Count odd as we count the chars.
def isPermutationOfPalindromeSolution2(phrase: str) -> bool:
  print('isPermutationOfPalindromeSolution2 > Input: ' + phrase)
  oddCount = 0
  frequencyTable = [0] * (ord('z') - ord('a') + 1)
  for char in phrase:
    index = getCharIndex(char)
    if index != -1:
      frequencyTable[index] += 1
      if frequencyTable[index] % 2 == 1:
        oddCount += 1
      else:
        oddCount -= 1
  return oddCount <= 1

# Solution 3:
# It uses binary representation of the letter (index in the alphabet a-z (0, 25))
# << This sets the 0 to 1 in the possition given from right to left. Example 1 << 19 = 00000000000010000000000000000000
# Apply an xor to the current bitVector with the number. 
# Example: 
# bitVector = 0 = (binary: 00000000000000000000000000000000)
# index = getCharIndex('t') = ord('t') - ord('a') = 116 - 97 = 19
# mask = 1 << 19 = 524288 (binary: 00000000000010000000000000000000)
# bitVector ^= mask = 0 ^ 524288 = 524288
# Result: bitVector = 524288 (binary: 00000000000010000000000000000000)

def isPermutationOfPalindromeSolution3(phrase: str) -> bool:
  print('isPermutationOfPalindromeSolution2 > Input: ' + phrase)
  bitVector = createBitVector(phrase)
  return hasAtMostOneBitSet(bitVector)

# Example:
# bitVector = 16384        # 0b00000000000000000100000000000000
# bitVector - 1 = 16383    # 0b00000000000000000011111111111111
# bitVector & (bitVector - 1) = 16384 & 16383 = 0
def hasAtMostOneBitSet(bitVector):
  return (bitVector & (bitVector - 1)) == 0

def toggle(bitVector, index):
  if index < 0: 
    return bitVector
  mask = 1 << index # Turn on the bit at the index position
  bitVector ^= mask # XOR the mask to the bitVector. If a bit in one position is 1 it will be set to 0
  return bitVector
  

def createBitVector(phrase):
  bitVector = 0
  for char in phrase:
    index = getCharIndex(char)
    bitVector = toggle(bitVector, index)
  return bitVector

if __name__ == '__main__':
  print('**** Permutation of Palidrome ****') 
  print('isPermutationOfPalindromeSolution1: ', isPermutationOfPalindromeSolution1('Tact coa'))
  print('isPermutationOfPalindromeSolution1: ', isPermutationOfPalindromeSolution1('raining'))
  print('isPermutationOfPalindromeSolution2: ', isPermutationOfPalindromeSolution2('Tact coa'))  
  print('isPermutationOfPalindromeSolution2: ', isPermutationOfPalindromeSolution2('raining'))    
  print('isPermutationOfPalindromeSolution3: ', isPermutationOfPalindromeSolution3('Tact coa'))  
  print('isPermutationOfPalindromeSolution3: ', isPermutationOfPalindromeSolution3('raining'))      