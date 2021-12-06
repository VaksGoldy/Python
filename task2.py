numbers = []
for el in range(1000):
    n = el % 2
    if n != 0:
        m = el ** 3
        numbers.append(m)
print(numbers)
for el in range(len(numbers)):
    sum = 0
    num = numbers[el]
    while num != 0:
        sum = sum + num % 10
        num = num // 10
    sum_d = sum % 7
    if sum_d == 0:
        print(sum)
for el in range(len(numbers)):
    numbers[el] = numbers[el] + 17
    sum = 0
    num = numbers[el]
    while num != 0:
        sum = sum + num % 10
        num = num // 10
    sum_d = sum % 7
    if sum_d == 0:
        print(sum)





