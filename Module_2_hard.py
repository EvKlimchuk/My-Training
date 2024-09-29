
def add_pair(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

my_dict = {}

for i in range(3,21):

    for k in range(1,i):

        for j in range(k+1,i):
            sum = k + j
            if i % sum == 0 and k != j:
                add_pair(my_dict, (i), (k))
                add_pair(my_dict, (i), (j))
                j +=1
            else:
                j +=1

for key, password in my_dict.items():
    print(f'{key} - {password}')










