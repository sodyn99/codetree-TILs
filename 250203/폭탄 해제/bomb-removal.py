unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Write your code here!

class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def print_bomb(self):
        print("code :", self.code)
        print("color :", self.color)
        print("second :", self.second)

bomb = Bomb(unlock_code, wire_color, seconds)
bomb.print_bomb()