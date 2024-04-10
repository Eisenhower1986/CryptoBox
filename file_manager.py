import os
from cryptography.fernet import Fernet

class FileManager:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def upload_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = self.cipher.encrypt(data)
        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_data)

    def download_file(self, file_path):
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = self.cipher.decrypt(encrypted_data)
        with open(file_path[:-4], 'wb') as f:
            f.write(decrypted_data)

    def delete_file(self, file_path):
        os.remove(file_path)

# Example usage
if __name__ == '__main__':
    key = b'your_key_here'  # Replace the example key here with your encryption key
    file_manager = FileManager(key)
    file_manager.upload_file('example.txt')
    file_manager.download_file('example.txt.enc')
    file_manager.delete_file('example.txt.enc')
