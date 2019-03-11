import hashlib
import hmac
from secrets import token_bytes
from base64 import b64encode,b64decode

def generate_key(size=32):
   '''
   Generate random key
   :param size: in bytes
   :return key:
   '''
   key = token_bytes(size)
   return key


def generate_tag(key, data):
    '''
    :param key: Key generated radomly
    :param data: data to be hashed
    :return: mac in base64
    '''
    mac = hmac.new(key, data, hashlib.sha512).digest()
    #mac = int.from_bytes(mac,byteorder='big')
    return b64encode(mac)


def verify(tag, data, key):
    '''
    Verifies if data has the same tag (if data has been modified)
    :param tag: original tag
    :param data: data to be verified
    :param key: key used for original tag
    :return: true if data is the same, false otherwise
    '''
    tag2 = generate_tag(key, data)
    return tag2 == tag


if __name__ == '__main__':
    msg = b"Un mensaje"
    msg2 = b"Un meensaje"
    key = generate_key()
    mac = generate_tag(key, msg)
    print("MAC: \n")
    print(mac)
    print("key: \n")
    print(key)
    print("verify: \n")
    print(verify(mac, msg2,key))
