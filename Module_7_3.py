import string
import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        # Перебираем названия файлов
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')
                words = text.split()
                all_words[file_name] = words
                return all_words

    def find(self, word):
        # Приводим слово к нижнему регистру
        word = word.lower()
        result = {}
        # Получаем словарь всех слов
        for file_name, words in self.get_all_words().items():
            position = words.index(word) + 1
            result[file_name] = position
        return result

    def count(self, word):

        word = word.lower()
        result = {}

        for file_name, words in self.get_all_words().items():
            # Считаем количество вхождений слова
            result[file_name] = words.count(word)
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
