
# Given a string and a non-negative int n, return a
# larger string that is n copies of the original string.

def string_times(str, n):
    z = ""
    for x in range(n):
        z = z + str
    return z

# Given a string and a non-negative int n, we'll say that
# the front of the string is the first 3 chars, or whatever
# is there if the string is less than length 3. Return n
# copies of the front;

def front_times(str, n):
    z = ""
    for x in range(n):
        z = z + str[:3]
    return z

# Given a string, return a new string made of every other char 
# starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    count = 0 
    z = ""
    for x in str: 
        if ( (count % 2) == 0):
            z += x
        count += 1
    return z

# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    z = ""
    for y in range(len(str) + 1):
        z += str[:y]
    return z

# Given a string, return the count of the number of times that a substring 
# length 2 appears in the string and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    z = str[len(str) - 2:]
    count = 0
    for x in range(len(str) - 2):
        if (str[x:x+2] == z):
            count += 1
    return count

# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0 
    for x in nums:
        if (x == 9):
            count += 1
    return count 

# Given an array of ints, return True if one of the first 4 elements in 
# the array is a 9. The array length may be less than 4.

def array_front9(nums):
    count = 0
    bool = False
    for x in nums: 
        if (count >= 4): 
            break 
        if (x == 9):
            bool = True 
        count += 1
    return bool

# Given an array of ints, return True if the sequence of numbers 1, 2, 3 
# appears in the array somewhere.

def array123(nums):
    bool = False
    for x in range(len(nums) - 2):
        if (nums[x] == 1):
            if (nums[x + 1] == 2): 
                if (nums[x + 2] == 3): 
                    bool = True
    return bool

# Given 2 strings, a and b, return the number of the positions where they 
# contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
# since the "xx", "aa", and "az" substrings appear in the same place in both 
# strings.

def string_match(a, b):
    count = 0
    length = 0
    if (len(a) >= len(b)):
        length = len(b)
    else:
        length = len(a)
    for x in range(length - 1): 
        if(a[x:x+2] == b[x:x+2]):
            count += 1
    return count
