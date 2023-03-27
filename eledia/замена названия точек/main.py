with open('text.txt', 'r', encoding='utf-8') as f:
    file = f.read()

file = file.replace('LU', 'P')
file = file.replace('LI', 'GI')
file = file.replace('ST', 'E')
file = file.replace('SP', 'RP')
file = file.replace('HT', 'C')
file = file.replace('SI', 'IG')
file = file.replace('BI', 'V')
file = file.replace('BL', 'V')
file = file.replace('KD', 'R')
file = file.replace('HC', 'MC')
file = file.replace('TH', 'TR')
file = file.replace('GB', 'VB')
file = file.replace('LV', 'F')
file = file.replace('GV', 'VG')
file = file.replace('CV', 'VC')
file = file.replace('TB', 'TR')

print(file)
with open('text_replace.txt', 'w', encoding='utf-8') as f:
    f.write(file)