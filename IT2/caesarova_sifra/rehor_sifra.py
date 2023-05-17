text = input("zadejte slova: ")
print(text)
kod = ""
for letter in text:
    if letter.isalpha():
        if ord(letter) >= 97:  # lowercase letters
            kod += chr((ord(letter) - 97 + 5) % 26 + 97)
        else:  # uppercase letters
            kod += chr((ord(letter) - 65 + 5) % 26 + 65)
    else:
        kod += letter
print(kod)
