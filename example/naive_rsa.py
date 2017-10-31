#!/usr/bin/env python3

from mod import Mod


def main():
    print("Simplified/naive RSA implementation")

    # Keys definition
    public_key = Mod(3, 1287302641)
    private_key = Mod(858153923, public_key.modulo)

    # Message
    message = 666
    print("raw message:", message)

    # RSA encryption
    encrypted = message**public_key
    print("simplified RSA encrypted message:", encrypted)

    # RSA decryption
    decrypted = encrypted**private_key
    print("simplified RSA decrypted message:", decrypted)


if __name__ == '__main__':
    main()
