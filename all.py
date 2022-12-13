# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать
# это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

some_list = [1,4,5,2,3,9,8,11,0,6,25]
some_list.sort()
result_list = []
count = 0
for i in range(len(some_list) - 1):
    if some_list[i] + 1 == some_list[i + 1]:
        count += 1
        if i == len(some_list) - 2 and count != 0:
            result_list.append(f'{some_list[i + 1] - count}-{some_list[i + 1]}')
    else:
        if count == 0:
            result_list.append(some_list[i])
        else:
            result_list.append(f'{some_list[i] - count}-{some_list[i]}')
            count = 0
        if i == len(some_list) - 2 and count == 0:
            result_list.append(some_list[i + 1])


result_str = ','.join(str(x) for x in result_list)
print(result_str)


#2
""" Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это
множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4" """

import re
def compress(file, result):
    with open(file, 'r', encoding='utf-8') as text:
        with open(result, 'w', encoding='utf-8') as res:
            inp_str = text.readline()
            flag = 0
            for i in inp_str:
                if re.search('[A-Z]', i):
                    flag += 0
                else:
                    flag += 1
            if flag == 0:
                ind = 0
                count = 1
                while ind < len(inp_str) - 1:
                    if inp_str[ind] == inp_str[ind + 1]:
                        count += 1
                    else:
                        if count == 1:
                            res.write(inp_str[ind])
                        else:
                            res.write(str(count) + inp_str[ind])
                        count = 1
                    ind += 1

                if ind == len(inp_str) - 1:
                    if inp_str[ind] == inp_str[ind - 1]:
                        res.write(str(count) + inp_str[ind])
                    else:
                        if count == 1:
                            res.write(inp_str[ind])
                            
            else:
                print('Некорректный ввод')

def decompress(file, result):
    with open(file, 'r', encoding='utf-8') as text:
        with open(result, 'w', encoding='utf-8') as res:
            inp_str = text.readline()
            flag = 0
            for i in inp_str:
                if re.search('[A-Z]', i) or i.isdigit():
                     flag += 0
                else:
                     flag += 1
            if flag == 0:
                count = ''
                for letter in inp_str:
                    if letter.isdigit():
                        count += letter
                    else:
                        if count != '':
                            res.write(int(count) * letter)
                        else:
                            res.write(letter)
                        count = ''
            else:
                print('Некорректный ввод')

#compress('input.txt', 'output.txt')
decompress('output.txt', 'input.txt')




