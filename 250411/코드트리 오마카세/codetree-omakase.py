from collections import deque

L, Q = map(int, input().split()) # 초밥 벨트 길이, 명령 수
orders = []
sushis = [[] for i in range(L)]
people = {}
# mode, t, x, name, n
for _ in range(Q):
    mode, t, *p = input().split()
    mode, t = map(int, [mode, t])
    orders.append([mode, t, p])

def eat(t0, t):
  #(x, n)
  remove_people = []
  for person, value in people.items():
    for i in range(len(sushis)):
      person_x, person_n = value[0], value[1]
      if (i > person_x and t - t0 >= L - i + person_x) or (i <= person_x and person_x -  i < t - t0):
        while person in sushis[i]:
          sushis[i].remove(person)
          person_n -= 1
      value[1] = person_n
      if person_n == 0:
        remove_people.append(person)
  for person in remove_people:
    people.pop(person, None)

t = 0
tf = 0
while orders:
  t0 = t
  order = orders.pop(0)
  mode, t, p = order[0], order[1], order[2]
  if len(orders) > 0:
    tf = orders[0][1]
  else:
    tf = t + 1
  sushis = sushis[-((t-t0)%L):] + sushis[:L-((t-t0)%L)] if 0 < (t-t0)%L else sushis
  if mode == 100:
    x, name = int(p[0]), p[1]
    sushis[x].append(name)
  elif mode == 200:
    x, name, n = int(p[0]), p[1], int(p[2])
    people[name] = [x, n]
  eat(t, tf)
  if mode == 300:
    num_sushis = sum([len(sushi) for sushi in sushis])
    num_people = len(people)
    print(num_people, num_sushis)

