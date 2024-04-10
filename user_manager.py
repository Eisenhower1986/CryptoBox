class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = password

    def authenticate_user(self, username, password):
        if username not in self.users or self.users[username] != password:
            raise ValueError("Invalid username or password")
        return True

    def change_password(self, username, new_password):
        if username not in self.users:
            raise ValueError("User does not exist")
        self.users[username] = new_password

    def delete_user(self, username):
        if username not in self.users:
            raise ValueError("User does not exist")
        del self.users[username]

# Example usage
if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.create_user('user1', 'password1')
    user_manager.authenticate_user('user1', 'password1')
    user_manager.change_password('user1', 'new_password')
    user_manager.delete_user('user1')
