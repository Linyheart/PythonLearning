import sys
import os
import glob
import time
path = sys.argv[1]
suffix = sys.argv[2]
limit = sys.argv[3]
print(path)
print(suffix)
print(limit)
os.chdir(path)
fileList = glob.glob('*.' + suffix)
print(fileList)
aimFile = []
fileSize = []
for i in range(0, len(fileList)):
    fileSize.append(round(os.path.getsize(fileList[i]) / int(1024 * 1024)))
    print(round(os.path.getsize(fileList[i]) / float(1024 * 1024)))
    if os.path.getsize(fileList[i]) / float(1024 * 1024) > int(limit):
        aimFile.append(i)
    print(aimFile)
    print(fileSize)

logLines = []
logLines.append('run at: ' + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + '\n')
logLines.append(suffix + ' files larger than ' + limit + 'MB in ' + path + '\n')
for i in range(0, len(aimFile)):
    logLines.append(str(i + 1) + '    ' + path + '\\' + fileList[aimFile[i]] + '    ' + str(fileSize[aimFile[i]]) + 'MB' + '\n')
logLines.append('\n')

print(logLines)

log = open('big_files.log', 'a')
log.writelines(logLines)
