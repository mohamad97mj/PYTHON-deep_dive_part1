def average():
    total = count = 0

    def add(n):
        nonlocal total, count
        total = total + n
        count = count + 1
        return total / count

    return add


a = average()
print(a(10))
print(a(20))
print(a(30))
