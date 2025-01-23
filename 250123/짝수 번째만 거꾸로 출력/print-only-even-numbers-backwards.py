a = input()

print(
    a[
        -1 if len(a) % 2 == 0 else -2::-2
    ]
)