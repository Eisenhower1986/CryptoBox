from cryptography.fernet import Fernet
import os

class CryptoBox:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = self.cipher.encrypt(data)
        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_data)
        os.remove(file_path)

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted_data = self.cipher.decrypt(data)
        with open(file_path[:-4], 'wb') as f:
            f.write(decrypted_data)
        os.remove(file_path)

# Example usage
if __name__ == '__main__':
    crypto_box = CryptoBox()
    crypto_box.encrypt_file('example.txt')
    crypto_box.decrypt_file('example.txt.enc')
