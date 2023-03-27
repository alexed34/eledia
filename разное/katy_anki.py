
import csv

with open('text.txt', 'r', encoding='utf-8') as f:
    file = f.read()
file = file.split('\n\n')
text = []
for i in file:

    if '----' in i:
        i = f'\n{i}'
        text = '<br> '.join(text)
        if text:
            with open('text2.csv', 'a', encoding='utf-8', newline='\n') as f:
                file_writer = csv.writer(f, delimiter = "&", lineterminator="\r")
                file_writer.writerow(text.split('----'))

        print(text)
        text = []
    i = i.lstrip('\n')
    i = i.replace('\n', '<br> ')
    # i = i.replace('\r', '</br> ')
    # i = i.split('----')
    text.append(i)
    # print(text)