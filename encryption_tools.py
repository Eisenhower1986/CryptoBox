from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()

# Example usage
if __name__ == '__main__':
    key = generate_key()
    data = "Hello, world!"
    encrypted_data = encrypt_data(data, key)
    decrypted_data = decrypt_data(encrypted_data, key)
    print("Original data:", data)
    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)
