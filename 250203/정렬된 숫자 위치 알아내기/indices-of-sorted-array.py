n = int(input())
s = list(map(int, input().split()))

# Write your code here!

class Sequence:
    def __init__(self, id, element, new_id=0):
        self.id = id
        self.element = element
        self.new_id = new_id

sequences = [Sequence(idx, element) for idx, element in enumerate(s, start=1)]

sequences.sort(key=lambda x: (x.element, x.id))

for new_idx, sequence in enumerate(sequences, start=1):
    sequence.new_id = new_idx

sequences.sort(key=lambda x: x.id)

for sequence in sequences:
    print(sequence.new_id, end=" ")
