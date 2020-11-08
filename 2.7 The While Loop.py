while True:
    name = input("Enter your name:\n")
    if len(name) >= 2 and name.isprintable() and name.isalpha():
        break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

l = [1, 2, 3]
index = 0
val = 10
while index < len(l):
    if l[index] == val:
        break
    index += 1
else:
    l.append(val)


print(l)