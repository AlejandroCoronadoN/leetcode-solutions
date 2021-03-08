class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
      """ Given a str of numbers, this function decode that string into a
      correponding secuence of letters represented by a phone number. 
      Each letter represent a sequence of character that can appera in combination with the subsequent numbers.
      
      This function traverse the string and for each number it get the collection of letters 
      represented by this number and then it compare it with the mapping function of the subsequent 
      numbers until we run out of numbers.
      
      Special cases: 
      ! Dont use 1 
      ! Empty string
      ! just one char 
      TODO  Dunamic programming
      
      """
      numbers_dict = {'2': ['a','b','c'],
                      '3': ['d','e','f'],
                      '4': ['g','h','i'],
                      '5': ['j','k','l'],
                      '6': ['m','n','o'],
                      '7': ['p','q','r', 's'],
                      '8': ['t','u', 'v'],
                      '9': ['w','x', 'y', 'z']}
      
      solutions:
      
      return self.letterCombinations_rec(digits, numbers_dict)

  def letterCombinations_rec(digits, numbers_dict):
    if len(digits) ==1:
      return numbers_dict[digits[0]]
    
    else:
      for n in digits:
        letter_it = numbers_dict[n]
        combiantions = []
        if digits in  solutions.keys():
          combinations = solutions[digits]
        else:          
          for d in letter_it: #d: abc -> d: def -> [ghi] combinations = d.ghi  e.ghi f.ghi
            for r in self.letterCombinations_rec(digits[1:], numbers_dict):
              combiantions.append(d + r)
          solutions[digits] =  combinations
        return combiantions
