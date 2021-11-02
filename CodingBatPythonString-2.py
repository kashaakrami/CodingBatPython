# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  x = ""
  for element in str:
    x += element + element
  return x

# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  counter = 0
  for x in range(len(str) - 1): 
    if str[x:x+2] == "hi":
      counter += 1
  return counter

# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  catcount = 0
  dogcount = 0
  for x in range(len(str) - 1): 
    if str[x:x+3] == "cat":
      catcount += 1
  for x in range(len(str) - 1): 
    if str[x:x+3] == "dog":
      dogcount += 1
  
  if(catcount == dogcount):
    return True
  else: 
    return False

# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
  codecount = 0
  for x in range(len(str) - 3): 
    if (str[x:x+2] == "co" and str[x+3] == "e"):
      codecount += 1
  return codecount

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
  if ( len(a) <= len(b)):
    if (b[-len(a):].lower()  == a.lower() ): 
      return True
  if ( len(b) < len(a)):
    if (a[-len(b):].lower() == b.lower() ): 
      return True
  return False

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
  for x in range(len(str)):
    if (str[x:x+3] =="xyz" and str[x-1] != "."):
      return True
  return False