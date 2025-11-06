// Determine if all the characters in the string are unique without data structure

// Solution 1 O(N^2)
function solution1(s) { 
  for (let i = 0; i < s.length; i++) { 
    for (let j = i + 1; j < s.length; j++) {
      if (s.charAt(i) === s.charAt(j)) {
        return false
      }
    }
  }
  return true
}

// Solution 2 O(N)
function solution2(s) { 
  let charSetArr = []
  for (let i = 0; i < s.length; i++) {
    let val = s.charAt(i).charCodeAt(0)
    if (charSetArr[val] === true) {
      return false
    }
    charSetArr[val] = true
  }
  return true
}

console.log("repeated: ", solution1("repeated"));
console.log("character: ", solution1("character"));
console.log("body", solution1("body"))
console.log("rainbow", solution1("rainbow"));


console.log("repeated: ", solution2("repeated"));
console.log("character: ", solution2("character"));
console.log("body", solution2("body"));
console.log("rainbow", solution2("rainbow"));