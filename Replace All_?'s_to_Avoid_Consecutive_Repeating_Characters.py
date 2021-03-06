class Solution:
  """
  Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.
  It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
  Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
  """
  def modifyString(self, s: str) -> str:
    i=0
    while i <= len(s)-1:
      if s[i] =='?':
        if i > 0:
          if i < len(s) -1:
            for j in range(97, 97+25): 
              if s[i-1] != chr(j) and s[i+1] != chr(j):
                s = list(s)
                s[i] = chr(j)
                s = ''.join(s)
                break
          else:
            for j in range(97, 97+25): 
              if s[i-1] != chr(j):
                s = list(s)
                s[i] = chr(j)
                s = ''.join(s)
                break
        else:
          for j in range(97, 97+25): 
            if i < len(s) -1:
              if s[i+1] != chr(j):
                s = list(s)
                s[i] = chr(j)
                s = ''.join(s)
                break
            else:
              s = list(s)
              s[i] = chr(97)
              s = ''.join(s)
              break
            
      i+=1
    return s
  
  
class Solution:
    def modifyString(self, s: str) -> str:
        res, prev = "", '?'
        for i, c in enumerate(s):
            next = s[i + 1] if i + 1 < len(s) else '?'
            prev = c if c != '?' else {'a', 'b', 'c'}.difference({prev, next}).pop()
            res += prev
        return res