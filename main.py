import random
import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

non_letters = numbers + symbols

print("Welcome to the PyPassword!\n")

while True:
  print("############\n")
  
  pass_length = int(input("Password Length? (16+ characters long recommended - Default: 24):\n") or 24)
  
  pass_count = int(input("How many passwords do you need? (MIN. 1 - Default: 10)") or 10)
  
  count_map = {
    'count_letters' : math.ceil(0.6 * pass_length),
    'count_numbers' : math.ceil(0.2 * pass_length),
    'count_symbols' : math.ceil(0.2 * pass_length)
  }
  
  print("\n############\n")
  
  print('Passwords Generated Successfully!\n')
  password_array = []
  
  for rep in range(0, pass_count):
    new_password = []
    
    for item in range(1, count_map['count_letters']):
      new_char = letters[random.randrange(0, len(letters) - 1)]
      new_password.append(new_char)
      
    for item in range(1, count_map['count_numbers']):
      new_char = numbers[random.randrange(0, len(numbers) - 1)]
      new_password.append(new_char)
    
    for item in range(1, count_map['count_symbols']):
      new_char = symbols[random.randrange(0, len(symbols) - 1)]
      new_password.append(new_char)
    
    while True:
      legible = True
      random.shuffle(new_password)
      
      for x in range(0,len(new_password) - 2):
        if new_password[0] in non_letters or (new_password[x] in non_letters and new_password[x+1] in non_letters):
          legible = False
  
      if legible:
        break
    
    print(f"{rep} - {''.join(new_password)}\n")
    password_array.append(''.join(new_password))

  if input('Generate more passwords? (Y)es or (N)o ').lower() == 'n':
    break;