def a(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
print(a(int(input("Введите число от 0 до 1000: "))))