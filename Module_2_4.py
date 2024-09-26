numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    if numbers[i] == 1:
        i += 1
    else:
        for j in (2, numbers[i] // 2 + 1):
            if numbers[i] % j == 0:
                not_primes.append(numbers[i])
                break
        else:
            primes.append(numbers[i])
print('Primes: ', primes)
print('Not primes: ', not_primes)
