from base64 import b64encode, b64decode
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


def generate_keys():
    '''Genera llave pública y privada con numeros primos de 2048 bits y una llave publica e = 65537
        regresa llave publica, privada y modulo
    '''
    from Crypto.PublicKey import RSA
    keyPair = RSA.generate(bits=2048,e = 65537)
    print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
    print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")
    return keyPair.e,keyPair.d,keyPair.n

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return: private key and public key also module
    '''

    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    return private_key, public_key,new_key.n



def sign_data(private_key, data):
    '''
    param: private_key in PEM format
    param: Data to be signed in base64
    return: base64 encoded signature
    '''
    from Crypto.PublicKey import RSA

    from Crypto.Hash import SHA256
    rsakey = RSA.importKey(private_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # It's being assumed the data is base64 encoded, so it's decoded before updating the digest
    digest.update(b64decode(data))
    sign = signer.sign(digest)
    return b64encode(sign)

def verify_sign(public_key, signature, data):
    '''
    Verifies with a public key from whom the data came that it was indeed
    signed by their private key
    param: public_key in PEM format
    param: signature String signature to be verified in base64
     param: data to be signed
    return: Boolean. True if the signature is valid; False otherwise.
    '''
    from Crypto.PublicKey import RSA
    from Crypto.Signature import PKCS1_v1_5
    from Crypto.Hash import SHA256
    from base64 import b64decode
    rsakey = RSA.importKey(public_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(b64decode(data))
    if signer.verify(digest, b64decode(signature)):
        return True
    return False

def verify(msg,signature,public_key,n):
    from hashlib import sha512
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    hashFromSignature = pow(signature, public_key, n)
    print("Signature valid:", hash == hashFromSignature)

def sign(msg,private_key,n):
    from hashlib import sha512
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    signature = pow(hash, private_key, n)
    print("Signature:", hex(signature))
    return signature


if __name__ == '__main__':
    msg = b'A message for signing'
    #private, public,n = generate_keys()
    private, public, n = generate_RSA()
    #signature = sign(msg,private,n)
    signature = sign_data(private,b64encode(msg))
    #verify(msg,signature,public,n)
    print(verify_sign(public,signature,b64encode(msg)))

