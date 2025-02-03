secret_code, meeting_point, time = input().split()
time = int(time)

# Write your code here!

class Secret:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

    def print_secret(self):
        print("secret code :", self.code)
        print("meeting point :", self.point)
        print("time :", self.time)
    
secret = Secret(secret_code, meeting_point, time)
secret.print_secret()

