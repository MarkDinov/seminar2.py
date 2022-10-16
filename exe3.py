# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072
n = int(input())
res = 0
for i in range(1, n + 1):
    res += (1 + (1 / i))**i
print(round(res, 3))