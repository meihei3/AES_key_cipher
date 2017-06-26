# AES_key_cipher
This Library is encoding inputed text with AES cipher, and decode. Then, you use your own key.

## Requirement
Python 3.5.2  
pycrypto 2.6.1

## Usage
```
from CipherTools import cipher_decode
from CipherTools import cipher_encode
from CipherTools import encode_base64

if __name__ == '__main__':
    key = encode_base64(input('key >> '))
    # type of key is only base64.
    data = input('data >> ')
    crypto_data = cipher_encode(data, key)

    print(cipher_decode(crypto_data, key))

```

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
