from encryption_tools import encrypt_data, decrypt_data
from key_manager import KeyManager
from file_manager import FileManager
from config import Config

def process_data(data):
    key_manager = KeyManager(Config.KEY_FILE)
    key = key_manager.get_key()

    encrypted_data = encrypt_data(data, key)
    decrypted_data = decrypt_data(encrypted_data, key)

    return decrypted_data

# Example usage
if __name__ == '__main__':
    data = "Sensitive data"
    processed_data = process_data(data)
    print("Original data:", data)
    print("Processed data:", processed_data)
