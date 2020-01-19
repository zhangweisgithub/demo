# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import json

SECRET_KEY = "a7c70203125e0149"


class AESCrypto(object):
    AES_CBC_KEY = bytes(SECRET_KEY, "utf-8")

    @classmethod
    def encrypt(cls, data, mode='cbc'):
        func_name = '{}_encrypt'.format(mode)
        func = getattr(cls, func_name)
        return func(data)

    @classmethod
    def decrypt(cls, data, mode='cbc'):
        func_name = '{}_decrypt'.format(mode)
        func = getattr(cls, func_name)
        return func(data)

    @staticmethod
    def pkcs7_padding(data):
        if not isinstance(data, bytes):
            data = data.encode()
            print(data)

        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        padded_data = padder.update(data) + padder.finalize()

        return padded_data

    @classmethod
    def cbc_encrypt(cls, data):
        if not isinstance(data, bytes):
            data = data.encode()

        cipher = Cipher(algorithms.AES(cls.AES_CBC_KEY),
                        modes.CBC(cls.AES_CBC_KEY),
                        backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = encryptor.update(cls.pkcs7_padding(data))
        en_data = base64.b64encode(padded_data).decode('utf8')
        return en_data

    @classmethod
    def cbc_decrypt(cls, data):
        data = base64.b64decode(data)
        if not isinstance(data, bytes):
            data = data.encode()

        cipher = Cipher(algorithms.AES(cls.AES_CBC_KEY),
                        modes.CBC(cls.AES_CBC_KEY),
                        backend=default_backend())
        decryptor = cipher.decryptor()

        uppaded_data = cls.pkcs7_unpadding(decryptor.update(data))

        uppaded_data = uppaded_data.decode()
        return uppaded_data

    @staticmethod
    def pkcs7_unpadding(padded_data):
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data)

        try:
            uppadded_data = data + unpadder.finalize()
        except ValueError:
            raise Exception('无效的加密信息!')
        else:
            return uppadded_data


def encrypt_data(data):
    de = AESCrypto()
    en_data = de.cbc_encrypt(data)
    return en_data


def decrypt_data(token):
    de = AESCrypto()
    user_info = json.loads(de.cbc_decrypt(token))
    return user_info


if __name__ == "__main__":
    sf = AESCrypto()
    data = json.dumps(
        {"uidNumber": "16861", "displayName": "Zheng Zhenjia", "role": 0, "uid": "zhengzhenjia", "platform": 1,
         "timestamp": "1234567"})
    sn = encrypt_data(data)
    # sn = sf.cbc_encrypt(data)
    print(sn)
    # sb = sf.cbc_decrypt(sn)
    sb = decrypt_data(sn)
    print(sb)
