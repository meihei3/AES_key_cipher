# coding: utf-8

from CipherTools import cipher_decode
from CipherTools import cipher_encode
from CipherTools import encode_base64

test_file = 'test.cryptotxt'

if __name__ == '__main__':
    key = encode_base64(input('key >> '))
    data = input('data >> ')
    with open(test_file, 'wb') as f:
        f.write(cipher_encode(data, key))
    print('data saved.')

    key = encode_base64(input('key >> '))
    with open(test_file, 'rb') as f:
        crypto_data = f.readline()
        print(cipher_decode(crypto_data, key))
