MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Write your code here!

class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = [
    Agent(codenames[i], scores[i]) for i in range(MAX_N)
]

min_name = ""
min_score = 100
for agent in agents:
    if agent.score < min_score:
        min_name = agent.codename
        min_score = agent.score

print(min_name, min_score)