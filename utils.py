import os
import shutil

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def delete_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

# Example usage
if __name__ == '__main__':
    directory_name = 'test_directory'
    create_directory(directory_name)
    print(f"Directory '{directory_name}' created")
    delete_directory(directory_name)
    print(f"Directory '{directory_name}' deleted")
