def find_longest(strings):
  maxlen = 0
  for s in strings:
    if len(s) > maxlen:
      maxlen = len(s)
  return maxlen

strings = ['cat','fishing', 'nightmare', 'dog', 'masterpeice', 'shellfish']

result = find_longest(strings)
print(result)