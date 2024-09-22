print("Homework task 2")
my_dict = {'Taniya': 1981, 'Kirill': 1986, 'Arina':2002, 'Darya': 2003}
print('Dict:',my_dict)
print('Existing value: ',my_dict['Kirill'])
print('Non-existing value: ',my_dict.get('Mark'))
my_dict.update({'Mark': 1972,
                'Katrin': 1988})
t = my_dict.pop("Taniya")
print('Modified dictionary: ',my_dict)
print('Deleted value: ',t)
print('____________________________________')
print("Homework task 3")

my_set = {235,'box','box', 180,180,(195,196,197)}
print('Set: ',my_set)
my_set.add(1)
new_elements = {2,3}
my_set.update(new_elements)
my_set.remove((195,196,197))
print('Modified set: ',my_set)



