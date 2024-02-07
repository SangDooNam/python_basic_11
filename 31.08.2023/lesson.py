

# password = 'admin@%ę'
# encrypted_pass = ''

# for letter in password:
#     encrypted_pass += str(ord(letter))
#     # print(str(ord(letter)))

# password = 'Superdoo354032'
# encrypted_pass = ''

# for i in password:
#     encrypted_pass += str(ord(i))

# print(encrypted_pass)

# encrypted_pass = 83117112101114100111111515352485150

# decrypted_pass = ['']

# for i in str(encrypted_pass):
    
#     decrypted_pass += str(chr(int(i)))
    
# print(decrypted_pass)

# password = "SangDooNam354032!"

# encrypted_pass = [None] * len(password)

# for i, e in enumerate(password):
#     encrypted_pass[i] = ord(e)
    
# print(encrypted_pass)

# """[83, 97, 110, 103, 68, 111, 111, 78, 97, 109, 51, 53, 52, 48, 51, 50, 33]"""

# encrypted_pass_str = ",".join(map(str, encrypted_pass))



# result = int(encrypted_pass_str)

# print(result)

# print(chr(83))

# encrypted_pass_str = "".join(map(str, encrypted_pass))


password = "07d>T£0,Pi_x"

encrypted_pass = [ord(char) for char in password]

print(encrypted_pass)

# decrypted_pass = ''.join(chr(char) for char in encrypted_pass)
decrypted_pass = [chr(char) for char in encrypted_pass]

print(decrypted_pass)