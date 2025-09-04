class Student:

    def __init__(self, fio: str, rus: int, math: int, phys: int):
        self.fio = fio
        self.rus = rus
        self.math = math
        self.phys = phys

    def __str__(self):
        return "{0}: {1}, {2}, {3}".format(
            self.fio, self.rus,
            self.math, self.phys,
        )


def is_better(st1: Student, st2: Student):
    flag = False
    sum1 = st1.rus + st1.phys + st1.math
    sum2 = st2.phys + st2.math + st2.rus
    if sum1 != sum2:
        flag = sum1 > sum2
    else:
        if st1.math != st2.math:
            flag = st1.math > st2.math
        elif st1.phys != st2.phys:
            flag = st1.phys > st2.phys
    return flag


def sorting(lst: list[Student]):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(lst) - 1):
            if is_better(lst[i + 1], lst[i]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False


try:
    print('Список абитуриентов: ')
    file = input()
    print("Количество мест для поступления: ")
    n = int(input())
    with open(file, 'r', encoding='utf-8') as f:
        lst = f.readlines()
    lst = [[n for n in x.split(': ')] for x in lst]
    lst = [[i[0], i[1].split(', ')] for i in lst]
    list_st = []
    for i in range(0, len(lst)):
        list_st.append(Student(lst[i][0],
                               int(lst[i][1][0]), int(lst[i][1][1]), int(lst[i][1][2])))
    sorting(list_st)
    result = list_st[:n]

    with open('output.txt', 'w', encoding='utf-8') as file:
        for i in result:
            file.write(str(i) + '\n')
    print(*[str(i) + '\n' for i in result])
except:
    print("wrong format")
