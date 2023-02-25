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
      if not isinstance(key, int):
         raise ValueError(f'Key must be integer!')
         
      if not key >=1 and key <=25:
         raise ValueError(f'Key must be >=1 and <= 25!')
         
      self.key = key
      
      if not isinstance(secret_value, str):
         raise ValueError(f'Secret value must be ')

      if not secret_value.isascii():
         raise ValueError(f'Secret value must be ascii.')       
      
      if not secret_value.isalpha():
         raise ValueError(f'Secret value must be aplhabet.')

      self.secret_value = secret_value
   
   def access_secret_value(self, key):
      pass
   
   def update_key(self, old_key, new_key):
      pass
    
def test_init():
   # Testing the istance is created successfully with correct params.
   storage = EncryptedStorage(key=7, secret_value='LaZanzara')
   assert storage != None, f'''The instance is not created successfully'''
   
   # Testing a ValueError is thrown if the key is of the wrong type: testing for float.
   try:
      storage = EncryptedStorage(key=float(7), secret_value='LaZanzara')
      assert False, f'Instantiation must fail if key is not an int. Instantiation successful with key of type float.'
   except ValueError:
      pass # A ValueError must be raised if key is not int.
   
   # Testing a ValueError is thrown if the key is of the wrong type: testing for str.
   try:
      storage = EncryptedStorage(key='7', secret_value='LaZanzara')
      assert False, f'Instantiation must fail if key is not an int. Instantiation successful with key of type str.'
   except ValueError:
      pass # A ValueError must be raised if key is not int.
   
   # Testing a ValueError is thrown if the key is outside of the range [1, 25].
   try:
      storage = EncryptedStorage(key=0, secret_value='LaZanzara')
      assert False, f'Instantiation must fail if key < 1. Instantiation successful with key = 0.'
   except ValueError:
      pass # A ValueError must be raised if key is < 1.
   
   try:
      storage = EncryptedStorage(key=26, secret_value='LaZanzara')
      assert False, f'Instantiation must fail if key > 25. Instantiation successful with key = 26.'
   except ValueError:
      pass # A ValueError must be raised if key is > 25.

   
   # Testing a ValueError is thrown if the secret value is not ascii.
   try:
     storage = EncryptedStorage(key=9, secret_value='aèiou')
     assert False, f'''Instantiation must fail if secret value is not ascii. Instantiation successful with secret value = 'aèiou'.'''
   except ValueError:
     pass # A ValueError must be raised if secret value is not ascii.


   # Testing a ValueError is thrown if the secret value is ascii but not aplha.
   try:
     storage = EncryptedStorage(key=9, secret_value='aiou!.')
     assert False, f'''Instantiation must fail if secret value is ascii but. Instantiation successful with secret value = 'aiou!.' '''
   except ValueError:
     pass # A ValueError must be raised if secret value is ascii but not alpha.


def test_access_secret_value():
   storage = EncryptedStorage(key=7, secret_value='LaZanzara')
   
   # Checking that we are able to recover the secret value with the correct key.
   val_correct_key = storage.access_secret_value(key=7)
   assert val_correct_key == 'LaZanzara', f'''Problem recovering secret value, expected: 'LaZanzara', got '{val_correct_key}'.'''
   
   # Checking that the wrong key is giving out a different value of the correct length.
   val_wrong_key_1 = storage.access_secret_value(key=3)
   assert val_wrong_key_1 != 'LaZanzara', f'''The wrong key allows to return the secret value. Encryption key: 7, decryption key: 3'''
   assert len(val_wrong_key_1) == len('LaZanzara'), f'''Using the wrong key returns a string with unexpected length. Got: {len(val_wrong_key_1)}.'''
   
   val_wrong_key_2 = storage.access_secret_value(key=4)
   assert val_wrong_key_2 != 'LaZanzara', f'''The wrong key allows to return the secret value. Encryption key: 7, decryption key: 4.'''
   assert len(val_wrong_key_2) == len('LaZanzara'), f'''Using the wrong key returns a string with unexpected length. Got: {len(val_wrong_key_2)}.'''
   
   # Checking that using different wrong keys is returning different outputs.
   assert val_wrong_key_1 != val_wrong_key_2, f'''Using different keys produces the same output. Keys: 3, 4. Output: '{val_wrong_key_1}'.'''
   

def test_update_key():
   storage = EncryptedStorage(key=2, secret_value='abc')
   
   #Checking if we are able to update key and access with new key.
   storage.update_key(old_key=2, new_key=3)
   recovered_value_correct_key = storage.access_secret_value(key=3)
   assert recovered_value_correct_key == 'abc', f'''Problem recovering secret value, expeted 'dfg', got '{recovered_value_correct_key}'.'''
   
   #Cheking if secret value is change correctly.
   recovered_value_with_old_key = storage.acces_secret_value(key=3)
   assert recovered_value_with_old_key != 'abc', 'Old key must not return correct secret value, expected different value'
   
   #Checking if we try to update key with wrong key.
   storage.update_key(old_key=1,new_key=4)
   recovered_value_uncorrect_key = storage.access_secret_value(key=4)
   assert recovered_value_uncorrect_key != 'abc', ''' Secret value shouldn't be 'abc' '''
   assert storage.access_secret_value(key=3) == 'abc', '''Secret value shouldn't be change'''
   
   
def test_EncryptedStorage():
   # test_initation() [The implementation is not yet ready]
   # test_access_secret_value() [The implementation is not yet ready]
   # test_update_key() [The implementation is not yet ready]
   print('Passed')

   
test_EncryptedStorage()
