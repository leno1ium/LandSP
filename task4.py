# (*) Обработать текст программы на языке C#, заменив все фрагменты вида "переменная++"
# (с любым количеством пробелов вокруг символов '=' и '+') на фрагменты “переменная = переменная + 1".
# (Задача, обратная предыдущей.)

import sys

from colorama import Fore, Style


def replace_increment(modified_line: str):
    if '++' in modified_line:
        variable = modified_line[:modified_line.find('++')].rstrip()
        modified_line = f"{variable} = {variable.lstrip()} + 1;"
    return modified_line

file = 'input_4.3.txt'
try:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except:
    print('file error')
    sys.exit(1)
try:
    with open('output.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            original_line = line.rstrip()
            modified_line = original_line

            modified_line = replace_increment(modified_line)

            if modified_line != original_line:
                print(Fore.RED + modified_line + Style.RESET_ALL)
                file.write(modified_line + " (Изменено)\n")
            else:
                print(original_line)
                file.write(original_line + '\n')

except:
    print("wrong format")
