with open('text.txt', 'r', encoding='utf-8') as f:
    file = f.read()
with open('text2.txt', 'w', encoding='utf-8', newline='\n') as f:
    f.write('')

file = file.replace('?', '')
file = file.replace('?', '')
file = file.replace('(', '')
file = file.replace(')', '')
file = file.replace('’', '')
words = file.split()
words2 = set(words)
words3 = []
for word in words2:
    if len(word)>2:
        word = word.lower()
        words3.append(word)
        with open('text2.txt', 'a', encoding='utf-8') as f:
            f.write(word)
            f.write('\n')


print(words3)