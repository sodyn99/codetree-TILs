user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!

class User:
    def __init__(self, id="codetree", level=10):
        self.id = id
        self.level = level
    
    def print_user(self):
        print(f"user {self.id} lv {self.level}")
    
user = User()
user.print_user()

user.id, user.level = user2_id, user2_level
user.print_user()