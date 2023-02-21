'''
Implement the class EncryptedStorage, which stores a value encrypted with a key. The class
works in the following way:
When an EncryptedStorage is created, the user needs to specify a key, which is an int number
in the range [1, 25]. The user also needs to specify a string secret_value, which is a 
secret value that he wants to store in the EncryptedStorage.

*NOTE*: the string secret_value is supposed to only contain ascii letters, and no other
character (no punctuation, no letters with accent, no spaces, etc.)

1. At the moment the EncryptedStorage is created, the key is stored as a private attribute
   in the class instance, and it is used to encrypt the string secret_value through an
   instance of CaesarCipher. 

2. The class provides the method access_secret_value(key), which, if the entered key is
   correct, returns the encrypted secret_value after being decrypted with key. If the key is
   wrong, it returns a random string of the same length of secret_value, using key as a seed
   (so that the random string is the same every time the method is called with the same key).

 3.The class provides the method update_key(old_key, new_key) which updates the encryption
   key. If old_key is the correct key, then secret_value is decrypted using the old key, and
   re-encrypted using the new key. The new encrypted value and key are stored in the instance.
   If the old_key is wrong, then the method does nothing. NOTE: this method is not supposedto
   return or print anything in any case.

Here is an example of usage:
```
es = EncryptedStorage(key=4, secret_value='Culex')
es.access_secret_value(4) # returns 'Culex'
es.access_secret_value(8) # returns 'oxyim'
es.access_secret_value(10) # returns 'KcBEK'

es.update_key(old_key=5, new_key=6)
es.access_secret_value(4) # returns 'Culex'
es.access_secret_value(8) # returns 'oxyim' '''


import CesarChiper

class EncryptedStorage():
  def __init__(self, key, secret_value):
    key_value_dict = {}
    
    if key not in range(1,26) or not secret_value.isascii:
      print("uncorrect key,value")

    self.key = key
    self.secret_value = secret_value

    A = CesarChiper(key) # I get TypeError: 'module' object is not callable
    A.get_entrypted_text(plaintext=secret_value)

    key_value_dict.update[self.key:self.__A]

    print(key_value_dict)

  def access_secret_value(self, key):
    pass

  def update_key(self, old_key, new_key):
    pass
