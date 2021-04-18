import re

"""
. any single character
* zero or many number of repetition
+ one or many number of repetition
? zero or one repetition
\w match any single character other than special symbol.
\W match special characters.
\s match any single space.
\d match any single digit.
"""

match_output = re.match(r"shraddha.+", "shraddha")
print("match_output")

if match_output:
    print("pattern ===", match_output.group())
else:
    print("No pattern found")

search_result = re.search(r"vi.a.", "hi Viraj vikas", re.IGNORECASE)
print("search ===", search_result)
print("search ==", search_result.group())

findall_result = re.findall(r"vi.a.", "hi Viraj vikas vijay", re.IGNORECASE)
print("findall == ", findall_result)

# \w - match any single character other than special symbol.
o = re.search(r"hello \w+", "hello vikas@jamdar")
print("\w ===", o.group())

# \W - match special characters.
o = re.search(r"hello \W+", "hello @! #abc$^")
print("\W ===", o.group())

# \s - match any single space.
o = re.search(r"hello\s*", "hello ab")
print("\s==" + o.group() + "hii")

# \d - match any single digit.
o = re.search(r"hello \d*", "hello 12345")
print("\d===", o.group())

o = re.search(r"hello \d+", "hello 1 world")
print("\d==", o.group())

# ^ - check if string starts with.
o = re.search(r"^hello \d+", "hello 123 shraddha")
print("^ ==", o.group())

# $ ends with or match at end of string
s = re.search(r"hello \w*$", "shraddha hello work")
print("w$ ==", s.group())

# [] brackets meaning - set of characters
o = re.search(r"Age [0-7|a-d]", "Age 70")
print("[] example==", o.group())

# []^ (exclude given set) meaning in brackets exclude
o = re.search(r"Age [0-9]+", "Age 10")
print("[]^ example==", o.group())

# [] meaning of bracket is include
o = re.search(r"[A-Za-z0-9\W]+", "aA88!2@#")
print("[] example==", o.group())

""" \ escape character """
o = re.search(r"Age \\Wvikas", "Age \Wvikas")
print("\ example ==", o.group())

# + 1 or more repetitions
o = re.search(r"(Co)+kie", "Cokie")
print("+ ==", o.group())

# * 0 or more repetitions
o = re.search(r"(Co)*kie", "Cokie")
print("* ==", o.group())

# ? 0 or 1 repetitions
o = re.search(r"(Co)?kie", "Cokie")
print("?==", o.group())

# [min,max] min or max repetitions
o = re.search(r"ID \d{3,5}", "ID 1276678 shraddha")
print("[min,max] ==", o.group())

# {} 0 or 1 repetition
o = re.search(r"\d{8,8}", "ID12034678")
print("{} == ", o.group())
