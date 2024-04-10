from key_manager import KeyManager
from file_manager import FileManager
from user_manager import UserManager

def main():
    key_manager = KeyManager()
    key = key_manager.get_key()

    file_manager = FileManager(key)
    user_manager = UserManager()

    while True:
        print("\n1. Upload file\n2. Download file\n3. Delete file\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
                user_manager.authenticate_user(username, password)
                file_path = input("Enter file path to upload: ")
                file_manager.upload_file(file_path)
                print("File uploaded successfully")
            except ValueError as e:
                print(e)

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
                user_manager.authenticate_user(username, password)
                file_path = input("Enter file path to download: ")
                file_manager.download_file(file_path)
                print("File downloaded successfully")
            except ValueError as e:
                print(e)

        elif choice == '3':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            try:
                user_manager.authenticate_user(username, password)
                file_path = input("Enter file path to delete: ")
                file_manager.delete_file(file_path)
                print("File deleted successfully")
            except ValueError as e:
                print(e)

        elif choice == '4':
            break

if __name__ == '__main__':
    main()
