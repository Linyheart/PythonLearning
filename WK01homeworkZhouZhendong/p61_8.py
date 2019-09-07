table = [[0 for col in range(9)] for row in range(9)]
for i in range(1,10):
    for j in range(i,10):
        formula = str(i) + '×' + str(j) + '=' + str(i*j)
        exec('table[{}][{}] = {} '.format(i, j, i))
print(table)