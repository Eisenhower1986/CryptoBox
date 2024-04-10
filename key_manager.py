from cryptography.fernet import Fernet

class KeyManager:
    def __init__(self, key_file='key.key'):
        self.key_file = key_file
        self.load_key()

    def load_key(self):
        try:
            with open(self.key_file, 'rb') as f:
                self.key = f.read()
        except FileNotFoundError:
            self.generate_key()
            self.load_key()

    def generate_key(self):
        self.key = Fernet.generate_key()
        with open(self.key_file, 'wb') as f:
            f.write(self.key)

    def get_key(self):
        return self.key

# Example usage
if __name__ == '__main__':
    key_manager = KeyManager()
    print("Key:", key_manager.get_key())
