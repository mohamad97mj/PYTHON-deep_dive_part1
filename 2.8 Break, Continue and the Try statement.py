a = 0
b = 10

while a < 4:
    a += 1
    b -= 1
    print('--------------------------')
    try:
        a / b
    except ZeroDivisionError:
        print("division by zero")
        # continue
        break
    finally:
        print("always execute")

else:
    print("code executed without division by zero")
