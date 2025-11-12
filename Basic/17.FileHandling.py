# write data in file
with open('data.txt', 'w', encoding='utf-8') as file:
    file.write('Thuận\n')
    file.write('Khang\n')
    file.write('Kiệt\n')
    file.write('Quân\n')
    file.write('Phát\n')

with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')