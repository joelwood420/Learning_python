def is_palendrome(s: str) -> bool:
  cleaned = "".join(c.lower()
for c in s if c.isalnum())
  return cleaned == cleaned[::-1]

print(is_palendrome("racecar"))
print(is_palendrome("pirate"))
print(is_palendrome("A man, a plan, a canal: Panama"))
