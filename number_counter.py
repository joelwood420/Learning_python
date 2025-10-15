def number_counter(which, nums):
  if (which != "even" and which != "odd"):
    return -1

  result = 0
  for num in nums:
    if which == "even" and num % 2 == 0:
      result += 1
    if which == "odd" and num % 2 != 0 :
      result += 1
  return result

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user_choice = input("even or odd?")

number_counter(user_choice, nums)