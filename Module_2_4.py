numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0
for i in range(len(numbers)):
    if numbers[i] > 1:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                k +=1
        if k == 0:
            primes.append(numbers[i])
        else:
            k = 0
            not_primes.append(numbers[i])
print('Primes: ', primes)
print('Not Primes: ', not_primes)

print('___________________________________________')
# Option 2

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_1 = []
not_primes_1 = []


for i in range(len(numbers_1)):
    if numbers_1[i] > 1:
        for j in range(2, numbers_1[i]//2+1):
            if numbers[i] % j == 0:
                not_primes_1.append(numbers[i])
                break
        else:
            primes_1.append(numbers[i])

print('Primes: ', primes_1)
print('Not Primes: ', not_primes_1)

print('___________________________________________')
# Option 3 Using Flag is_prime

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_2 = []
not_primes_2 = []
is_prime = True
for i in range(len(numbers_2)):
    if numbers_2[i] > 1:
        for j in range(2, numbers_2[i]):
            if numbers_2[i] % j == 0:
                is_prime = False

        if is_prime:
            primes_2.append(numbers_2[i])

        else:
            is_prime = True
            not_primes_2.append(numbers_2[i])
print('Primes: ', primes_2)
print('Not Primes: ', not_primes_2)
