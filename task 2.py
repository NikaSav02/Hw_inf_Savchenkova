N = int(input("Введите количество чисел в списке "))
A = [ int(input("Введите число из списка ")) for i in range(N) ]
B = []
for j in range(N):
    j = min(A)
    B.append(j)
    A.remove(j)
print(B)