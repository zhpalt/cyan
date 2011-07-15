# coding=utf-8
# 生产40个50M大小的随机文件

import os
parentDir = 'c:\\tmpp\\'        # 父目录
fileNameBase = '50MbigFile'       # 子文件名
index = 0
# 创建父目录
if not os.path.exists(parentDir):
    os.makedirs(parentDir)
# 开始创建各个子文件
while index < 40:
    fileName = parentDir + fileNameBase + '_' + str(index)
    f = open(fileName, 'wb')
    for ii in range(1024 * 50 - 1):
        f.write(os.urandom(1024))
        f.flush()
    f.close
    index += 1
    print 'Has done %d' % index