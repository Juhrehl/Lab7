def is_str(word):
  while True:
    value = input(word)
    try:
      value = int(value)
      print("Try using a word instead!")
    except:
      break
  return value

def substr(word):
  print (word[::-1])

def main():
  word = is_str("Type a word to reverse them: ")
  substr(word)

main()