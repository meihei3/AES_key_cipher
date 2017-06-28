# AES_key_cipher
This Library is encoding inputed text with AES cipher, and decode. Then, you use your own key.

## Requirement
Python 3.5.2  
pycrypto 2.6.1

## Usage
```
<<<<<<< HEAD
from CipherTools import cipher_decode
from CipherTools import cipher_encode
from CipherTools import encode_base64

if __name__ == '__main__':
    key = encode_base64(input('key >> '))
    # type of key is only base64.
    data = input('data >> ')
    crypto_data = cipher_encode(data, key)

    print(cipher_decode(crypto_data, key))
=======
import CipherTools as ct

if __name__ == '__main__':
    key = input('key >> ')
    data = input('data >> ')
    crypto_data = ct.cipher_encode(data, key)

    print(ct.cipher_decode(crypto_data, key))
>>>>>>> 832c36cff19096d826a001090ed22fa621440836

```

## Licence

<<<<<<< HEAD
[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
=======
[MIT](https://github.com/yameholo/AES_key_cipher/blob/master/LICENSE.txt)
>>>>>>> 832c36cff19096d826a001090ed22fa621440836
