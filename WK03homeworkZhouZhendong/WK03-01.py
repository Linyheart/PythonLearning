import win32ui
import numpy
dlg = win32ui.CreateFileDialog(1)
dlg.DoModal()
filepath = dlg.GetPathName()
file = open(filepath, encoding="utf-8")
dataLine = file.readlines()
file.close()
for i in range(0, len(dataLine)):
    if dataLine[i][0] == '#':
        dataLine[i] = 'deleteThis'
    dataLine[i] = dataLine[i].replace("\n", '')
    if dataLine[i] == '':
        dataLine[i] = 'deleteThis'
dataLine = filter(lambda x: x != 'deleteThis', dataLine)
newDateLine = list(dataLine)
data = list(map(int, newDateLine))
print("数字个数："+str(len(data)))
print("最大值："+str(max(data)))
print("最小值："+str(min(data)))
print("和："+str(sum(data)))
print("平均值："+str(round(numpy.mean(data), 2))+"（保留两位小数）")
print("标准差："+str(round(numpy.std(data), 2))+"（保留两位小数）")

