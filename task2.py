# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

nums = int(input("Введите трехзначное число "))
num1 = (nums % 10)
num2 = (nums // 10) % 10
num3 = (nums // 10) // 10 % 10
print("Сумма цифр числа =", num1 + num2 + num3)