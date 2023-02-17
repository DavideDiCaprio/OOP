'''In this exercise you will implement the class CaesarCipher, which represents
the famous Caesar cipher, which encrypts a text by substituting each letter of
the input text with the letter k steps ahead in the alphabet (reference:
https://en.wikipedia.org/wiki/Caesar_cipher). The class has the following behaviour:

a. When instantiated, the key k needs to be specified and stored within the instance.
   The key k indicates how many letters ahead we are performing the shift. Ex:
   encrypting the letter ‘a’ with k=4 means replacing it with ‘e’ (which is the
   letter 4 steps forward in the alphabet). Encrypting with k=5 would replace it with
   the letter ‘f’ and so on and so forth.
b. The class offers the method get_encrypted_text(plaintext) which encrypts the string
   plaintext by substituting each letter with the letter k steps forward. The function
   returns the encrypted text.
c. The class offers the method get_decrypted_text(ciphertext) which deciphers the
   string ciphertext and returns the decrypted string.
d. The class has the method is_cipher_working() which will test if the encryption/
   decription mechanism is working properly. It performs the encryption of the string
   'QWERTY,asdfg.', then the encrypted text is decrypted and a check is performed to
   test wether after decryption we properly recover the initial string. Returns True
   if the initial string is identical to the result of the decryption, False otherwise.

*NOTE* 1: The shift will only happen for the letters in the text, not for punctuation,
        numbers or any other symbol.
        
*NOTE* 2: Please remember the alphabet has only 26 letters, so sometimes you need to
          cycle back to the beginning of the alphabet (ex: encrypting 'z' with k=4
          would result in 'd'. For more clarity: ...xyzabcdef...)


Here is an example:

```
cipher = CaesarCipher(k=4)
plaintext = 'La Zanzara è una famosa trasmissione radiofonica, condotta da Giuseppe Cruciani e David Parenzo.'

ciphertext = cipher.get_encrypted_text(plaintext=plaintext)
print(ciphertext) # prints: 'Pe Derdeve è yre jeqswe xvewqmwwmsri vehmsjsrmge, gsrhsxxe he Kmywitti Gvygmerm i Hezmh Tevirds.'

decrypted = cipher.get_decrypted_text(ciphertext=ciphertext)
print(decrypted) #prints: 'La Zanzara è una famosa trasmissione radiofonica, condotta da Giuseppe Cruciani e David Parenzo.'

cipher.is_cipher_working() # returns True.
```


'''
class CaesarCipher():
  def __init__(self, k):
    self.key = k
    
  def get_encrypted_text(self, plaintext):
   encrypted_text = []
   
   for l in plaintext:
      if ord(l) >= ord('a') and ord(l) <= ord('z'):
         encrypted_text.append(self.shift_letter(letter=l,shift=self.key))
         
      elif ord(l) >= ord('A') and ord(l) <= ord('Z'):
         encrypted_text.append(self.shift_letter(letter=l,shift=self.key))

      else:
        encrypted_text.append(l)
   return ''.join(encrypted_text)

  def get_decrypted_text(self, ciphertext):
    decrypted_text = []

    for l in ciphertext:
      if ord(l) >= ord('a') and ord(l) <= ord('z') or ord(l) >= ord('A') and ord(l) <= ord('Z'):
        decrypted_text.append(self.shift_letter(letter=l,shift= -self.key))
      else:
        decrypted_text.append(l)
    return ''.join(decrypted_text)
   
  def is_cipher_working(self):
    test_string = 'QWERTY,asdfg.'
    
    encrypted_text_test = self.get_encrypted_text(plaintext = test_string)
    decrypted_text_test = self.get_decrypted_text(ciphertext=encrypted_text_test)
    
    if decrypted_text_test == test_string:
      return True 
    return False
   
  def shift_value(self, val_to_shift, shift_amount, first_value, len_alphabet=26):
    if val_to_shift < first_value or val_to_shift >= first_value+len_alphabet:
      print('ERROR: the value to shift is outside of the expected range!')
      return
    return ((val_to_shift-first_value+shift_amount)%len_alphabet)+first_value
    
  def shift_letter(self, letter, shift):
    if not isinstance(shift,int):
      print('Error: shift must be integer.')
      return

    if not isinstance(letter,str):
      print('Error: letter must be an instance of str')
      return
      
    if len(letter) !=1:
      print(f'Error: letter must have  exactly one character. Found: {len(letter)}')
      return
      
    if not letter.isalpha():
      print(f'Error: not a letter. Found: {letter}.')
      return
      
    if not letter.isascii():
      print('Error: letter not ascii.')
      
    frist_value = None
    if letter.isupper():
      frist_value = ord('A')
      
    elif letter.islower():
      frist_value = ord('a')
      
    return chr(shift_value(val_to_shift=ord(letter), shift_amount=shift, first_value=frist_value,len_alphabet=26))
