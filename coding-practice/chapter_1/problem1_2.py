def sortString(s):
    return ''.join(sorted(s))

def permutation1(s1, s2):
    if len(s1) != len(s2):
        return False
    return sortString(s1) == sortString(s2)

def permutation2(s1, s2):
    if len(s1) != len(s2):
        return False
    letters = [0] * 128  # Assuming ASCII
    for char in s1:
        letters[ord(char)] += 1
    for char in s2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True

if __name__ == "__main__":
    print('SOLUTION 1: --------------------------')
    s1 = 'one'
    s2 = 'three'
    print(f'Are "{s1}" and "{s2}" permutations of each other? : {permutation1(s1, s2)}')
    s1 = 'listen'
    s2 = 'silent'
    print(f'Are "{s1}" and "{s2}" permutations of each other? : {permutation1(s1, s2)}')
    s1 = 'part'
    s2 = 'cart'
    print(f'Are "{s1}" and "{s2}" permutations of each other? : {permutation1(s1, s2)}')

    print('SOLUTION 2: --------------------------')
    s1 = 'one'
    s2 = 'three'
    print(f'Are "{s1}" and "{s2}" permutations of each other? : {permutation2(s1, s2)}')
    s1 = 'listen'
    s2 = 'silent'
    print(f'Are "{s1}" and "{s2}" permutations of each other? : {permutation2(s1, s2)}')
    s1 = 'part'
    s2 = 'cart'
    print(f'Are "{s1}" and "{s2}" permutations of each other? : {permutation2(s1, s2)}')