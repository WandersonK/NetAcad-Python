text = input("Enter your message: ")

while True:
    interval = int(input("Informe um intervalo de deslocamento entre 1 e 25: "))

    if interval < 1 or interval > 25:
        print("Intervalo inválido!")
    else:
        break


cipher = ''
for char in text:
    if not char.isalpha():
        cipher += str(char)
        continue
    code = ord(char) + interval
    if code > ord('Z') and char.isupper():
        if code > (ord('Z') + 1):#and interval > 1:
            resto = interval - (ord('Z') - ord(char)) - 1
            code = ord('A') + resto
        else:
            code = ord('A')

    elif code > ord('z') and char.islower():
        if code > (ord('z') + 1):
            resto = interval - (ord('z') - ord(char)) - 1
            code = ord('a') + resto
        else:
            code = ord('a')

    cipher += chr(code)

print(cipher)

