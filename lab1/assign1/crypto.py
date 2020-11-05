"""Assignment 1: Cryptography for CS41 Winter 2020.

Name: <JÓZSA BOGLÁRKA>
SUNet: <jbim1827>

"""
import utils
import string
import math

letters = string.ascii_letters
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

#################
# CAESAR CIPHER #
#################

def encrypt_caesar(plaintext):
    result = ''
    for p in plaintext:
        if p in uppercase:
            char_shifted = uppercase.index(p) + 3
            result += uppercase[char_shifted % 26]
        else:
            result += p
    return result
    

def decrypt_caesar(ciphertext):
    result = ''
    for c in ciphertext:
        if c in uppercase:
            char_shifted = uppercase.index(c) - 3
            result += uppercase[char_shifted % 26]
        else:
            result += c
    return result


###################
# VIGENERE CIPHER #
###################

def encrypt_vigenere(plaintext, keyword):
    key_length = len(keyword)
    key_as_int = [ord(i) for i in keyword]
    plaintext_int = [ord(i) for i in plaintext]
    result = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        result += chr(value + 65)
    return result

def decrypt_vigenere(ciphertext, keyword):
    key_length = len(keyword)
    key_as_int = [ord(i) for i in keyword]
    plaintext_int = [ord(i) for i in ciphertext]
    result = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] - key_as_int[i % key_length]) % 26
        result += chr(value + 65)
    return result


###################
# SCYTALE CIPHER #
###################

def encrypt_scytale(plaintext, circumference):
    text_len = len(plaintext)
    result = ''
    for i in range(circumference):
        slice_object = slice(i, text_len, circumference)
        result += plaintext[slice_object] 
    return result


def decrypt_scytale(ciphertext, circumference):
    text_len = len(ciphertext)
    decrypt_circumference = math.ceil(text_len/circumference)
    result = ''
    for i in range(decrypt_circumference):
        slice_object = slice(i, text_len, decrypt_circumference)
        result += ciphertext[slice_object] 
    return result


###################
# RAILFENCE CIPHER #
###################

def creaate_grid(text, num_rails):
    return [['\n' for i in range(len(text))] 
                  for j in range(num_rails)]

def encrypt_railfence(plaintext, num_rails):
    rail = creaate_grid(plaintext, num_rails)
      
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(plaintext)):  
        if (row == 0) or (row == num_rails - 1): 
            dir_down = not dir_down 
          
        rail[row][col] = plaintext[i] 
        col += 1

        if dir_down: 
            row += 1
        else: 
            row -= 1

    result = [] 
    for i in range(num_rails): 
        for j in range(len(plaintext)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result))

def decrypt_railfence(ciphertext, num_rails):
    rail = creaate_grid(ciphertext, num_rails) 
      
    dir_down = None
    row, col = 0, 0
       
    for i in range(len(ciphertext)): 
        if row == 0: 
            dir_down = True
        if row == num_rails - 1: 
            dir_down = False
          
        rail[row][col] = '*'
        col += 1
          
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    index = 0
    for i in range(num_rails): 
        for j in range(len(ciphertext)): 
            if ((rail[i][j] == '*') and
               (index < len(ciphertext))): 
                rail[i][j] = ciphertext[index] 
                index += 1
          
    result = [] 
    row, col = 0, 0

    for i in range(len(ciphertext)): 
        if row == 0: 
            dir_down = True
        if row == num_rails-1: 
            dir_down = False
              
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result))