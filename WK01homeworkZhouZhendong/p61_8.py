table = [[0 for col in range(10)] for row in range(10)]
for i in range(1, 10):
    for j in range(i, 10):
        formula = str(i) + '×' + str(j) + '=' + str(i*j)
        exec('table[{}][{}] = "{}" '.format(i, j, formula))
        exec('table[{}][{}] = "{}" '.format(j, i, formula))
tableFormat = input("请输入您需要的乘法表格式（目前支持：上三角，下三角，矩形块）：")
if tableFormat == "上三角":
    for m in range(0, 9):
        for n in range(1, 10):
            if m+n > 9:
                break
            print(str(table[n][m+n]) + "\t", end=' ')
        print("")
elif tableFormat == "下三角":
    for m in range(1, 10):
        for n in range(1, 10):
            if m < n:
                break
            print(str(table[n][m]) + "\t", end=' ')
        print("")
elif tableFormat == "矩形块":
    for m in range(1, 10):
        for n in range(1, 10):
            print(str(table[n][m]) + "\t", end=' ')
        print("")