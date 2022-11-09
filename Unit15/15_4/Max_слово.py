import re

# Ввод имени открываемого файла input()
nameFile = input('Название файла: ')

# Открытие open() и чтение read()
with open(nameFile, encoding='utf8') as f:
    text = f.read()

# Путем замены replace() уберем из текста символы, приведем к одному регистру lower()

for i in '!"\'#$%&()*+-.,/:;<=>?@[\\]^_{|}~':
    text = text.lower().replace(i, '')

# Разделим строку split()
text = text.split()

# Создаем словарь из слов длиной более трех символов и находим повторяющиеся
recurring = dict()
for word in text:
    if len(word) > 2:
        recurring[word] = recurring.get(word, 0) + 1

print('---'*45)
# Выводим слова, которые в тексте встречаются чаще других
print('Наиболее часто встречающееся слово (слова) из тех, что имеют размер более трех символов\n',
      [word for word in recurring if recurring[word] == max(recurring.values())])

# Создаем списки русских и английских слов
# без использования Python RegEx нужен цикл for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
regex = "[a-zA-Z]"
pattern = re.compile(regex)

WordsEN = []

for word in recurring:
    if pattern.search(word) is not None:
        WordsEN.append(word)

# Найдем наиболее длинное слово (слова) на английском языке
LongestWords = []

for word in WordsEN:
    if len(max(WordsEN, key=len)) == len(word):
        LongestWords.append(word)

print('---'*45)
print('Наиболее длинное слово (слова) на английском языке:\n', LongestWords)
print('---'*45)
