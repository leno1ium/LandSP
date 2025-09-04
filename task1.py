# Составить новый список чисел, отсортированных по возрастанию, из чисел переданного списка,
# встречающихся в исходном списке максимальное число раз, например:
# { 9, 3, 1, 3, 7, 7, 5, 3, 9, 9, 15, 12, 10 } → { 3, 9 }
import sys

try:
    with open('empty.txt', 'r') as f:
        string = f.read().strip().replace(',', ' ').split()
except:
    print("File not found")
    sys.exit(0)
try:
    list_1 = [int(x) for x in string]
    cnt = []
    for i in range(0, len(list_1)):
        cnt.append(list_1.count(list_1[i]))
    max_cnt = max(cnt)
    result = []
    for i in range(0, len(list_1)):
        if cnt[i] == max_cnt:
            if list_1[i] not in result:
                result.append(list_1[i])
    with open("output", "w") as file:
        file.write(str(sorted(result)))
except:
    with open("output", "w") as file:
        file.write("Wrong format")
    print("Wrong format")
