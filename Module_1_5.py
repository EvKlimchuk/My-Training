immutable_var = 2,"words",[3,8,8],False,1
print(immutable_var)
# immutable_var[-1] = 0
# элементы и их последовательность в кортеже имзенять нельзя, однако если элементом является лист
# то внутри листа вносить изменения можно. Кортеж можно также увеличивать добавляя к нему другой кортеж
# или путем повторения послдеовательности элементов с помощью умножения

mutable_list = ["Python development",'Module', "Introduction"]
mutable_list[-1] = 1
print(mutable_list)

