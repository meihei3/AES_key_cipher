# AES_key_cipher
This Library is encoding inputed text with AES cipher, and decode. Then, you use your own key.

## Requirement
Python 3.5.2  
pycrypto 2.6.1

## Usage
```
import CipherTools as ct

if __name__ == '__main__':
    key = input('key >> ')
    data = input('data >> ')
    crypto_data = ct.cipher_encode(data, key)

    print(ct.cipher_decode(crypto_data, key))
'''

## Licence
[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
