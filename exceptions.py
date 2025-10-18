# try:
#   x = 10 / 0
# except:
#   print("That didnt work")

try:
  answer = input('10 / ?')
  num = int(answer)
  print(10 / num)
except ZeroDivisionError as e:
  print("You can't divide by zero")
except ValueError as e:
  print("That's not a number")
  print(e)
finally:
  print("finally - this always runs")
