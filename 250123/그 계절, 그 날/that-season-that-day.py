Y, M, D = map(int, input().split())

# Write your code here!

def is_yoon(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def there_is(y, m, d):
    M_30 = [4, 6, 9, 11]
    M_31 = [1, 3, 5, 7, 8, 10, 12]
    M_yoon = [2]
    if m in M_30:
        return True if d in [i for i in range(1, 31)] else False
    elif m in M_31:
        return True if d in [i for i in range(1, 32)] else False
    elif m in M_yoon:
        if is_yoon(y):
            return True if d in [i for i in range(1, 30)] else False
        else:
            return True if d in [i for i in range(1, 29)] else False
    else:
        return False

def season(y, m, d):
    if there_is(y, m, d):
        if m in [3, 4, 5]:
            return "Spring"
        elif m in [6, 7, 8]:
            return "Summer"
        elif m in [9, 10, 11]:
            return "Fall"
        else:
            return "Winter"
    else:
        return(-1)

print(season(Y, M, D))

