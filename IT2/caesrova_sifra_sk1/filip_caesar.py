import time

def enkrypt(message, shift):
  result = ""
  for char in message:
    if char.isalpha():
      shift_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
      if char.islower():
        result += shift_char.lower()
      else:
        result += shift_char
    else:
      result += char
  return result

def dekrypt(message, shift):
  result = ""
  for char in message:
    if char.isalpha():
      shift_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
      if char.islower():
        result += shift_char.lower()
      else:
        result += shift_char
    else:
      result += char
  return result


print("Vítejte v Ceasorově šifře!")
time.sleep(1)
print("Chcete enkryptovat nebo DEKryptovat?")
time.sleep(1)
print('Zadejte 1 pro "Enkrypt" \n      2 to "Dekrypt".')
choice = int(input("Zadejte svojí možnost: "))
if choice != 1 and choice != 2:
  print("Invalid choice.")
  exit()
time.sleep(1)
message = input("Vaše zpráva: ")
time.sleep(1)
shift = int(input("Klíč: "))
time.sleep(1)

if choice == 1:
    result = enkrypt(message, shift)
    print(f"Your Encrypted message is {result}.")
elif choice == 2:
    result = dekrypt(message, shift)
    print(f"Your Decrypted message is {result}.")