class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                # Убираем пунктуацию
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(symbol, '')
                words = text.split()  # Разбиваем текст на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1
        return word_positions

    def count(self, word):
        word = word.lower()
        word_count = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word)
        return word_count


# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
