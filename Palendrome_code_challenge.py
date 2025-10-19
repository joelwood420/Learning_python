def is_palendrome(s: str) -> bool:
  cleaned = "".join(c.lower()
for c in s if c.isalnum())
  return cleaned == cleaned[::-1]

print(is_palendrome("racecar"))
print(is_palendrome("pirate"))
print(is_palendrome("A man, a plan, a canal: Panama"))


def is_palendrome1(teststr):
  temp = teststr.lower() # Call the lower() method
  newstr = ""
  for c in temp:
    if c.isalnum():
      newstr += c
  reversestr = newstr[::-1]
  return reversestr == newstr # Move return statement outside the loop

print(is_palendrome1("racecar"))
print(is_palendrome1("pirate"))
print(is_palendrome1("A man, a plan, a canal: Panama"))
