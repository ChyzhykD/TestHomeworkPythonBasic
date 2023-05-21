def show_bigger(a, b):
    if a > b:
        return a
    else:
        return b


def show_smaller(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


def show_abs(num):
    if num >= 0:
        return num
    else:
        return -num


def show_sum(a, b):
    print("Сума значень:", a + b)


def show_sign(num):
    if num > 0:
        print("Число позитивне")
    elif num == 0:
        print("Число нульове")
    else:
        print("Число негативне")


# Приклад виклику функцій:
x = 5
y = 8
z = -3

bigger_value = show_bigger(x, y)
print("Більше число:", bigger_value)

smaller_value = show_smaller(x, y, z)
print("Менше число:", smaller_value)

abs_value = show_abs(z)
print("Модуль числа:", abs_value)

show_sum(x, y)

show_sign(z)
