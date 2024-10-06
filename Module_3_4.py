# Самостоятельная работа по уроку "Произвольное число параметров"

# Задача "Однокоренные"

def single_root_word(root_word, *other_words):
    same_words= []
    root_word.lower()
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
        elif word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


result_1 = single_root_word('rich', 'richest', 'orichalcum','cheers', 'richies')
result_2 = single_root_word('Disablement','Able', 'Mable', 'Disable', 'Bagel')
print(result_1)
print(result_2)

