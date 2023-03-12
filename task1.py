# Найдите сумму цифр трехзначного числа.

digit = int(input())
digit_sum = digit // 100 + digit // 10 % 10 + digit % 10
print(digit_sum)