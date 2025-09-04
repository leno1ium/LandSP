with open('input_2.2', 'r') as f:
    lst = f.readlines()

try:
    lst = [[int(n) for n in x.split()] for x in lst]
    flag_inc = True
    flag_dec = True
    result = True

    for i in range(1, len(lst[0])):
        if flag_dec or flag_inc:
            if flag_inc:
                if i % 2 == 0:
                    flag_inc = all(lst[j-1][i] > lst[j][i] for j in range(len(lst) - 1, 0, -1))
                else:
                    flag_inc = all(lst[j-1][i] < lst[j][i] for j in range(1, len(lst)))
            if flag_dec:
                if i % 2 == 0:
                    flag_dec = all(lst[j-1][i] < lst[j][i] for j in range(len(lst) - 1, 0, -1))
                else:
                    flag_dec = all(lst[j-1][i] > lst[j][i] for j in range(1, len(lst)))
        else:
            break
    result = flag_dec or flag_inc
    with open("output", "w") as file:
        file.write(str(result))
except:
    with open("output", "w") as file:
        file.write("wrong format")
        print("wrong format")
