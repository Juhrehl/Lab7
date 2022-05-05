def is_int(number):
  value = 0
  while True:
    try:
      value = int(input(number))
      break
    except:
      print("Try using a number instead!")
  return value
    
def is_str(word):
  while True:
    value = input(word)
    try:
      value = int(value)
      print("Try using a word instead!")
    except:
      break
  return value

def substr(word, number, distance):
  print(word[number:distance])

def main():
  while True:
    word = is_str ("Choose a word: ")
    length = len(word)
    number = is_int("Put a value of the word you want to start at: ")
    distance = is_int ("Put a value of the word you want to end at: ")

    if distance > length and number <= 0:
      print ("Your value should be greater than or is less than 0 ")
    elif distance <= length and number >= 0:
      substr(word, number, distance)
      break

main()