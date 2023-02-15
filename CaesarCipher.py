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

  def __init__(self,k):
    self.key = k
  
  def get_encrypted_text(self,plaintext):
    pass

  def get_decrypted_text(self,ciphertext):
    pass

  def is_cipher_working(self):
    pass
