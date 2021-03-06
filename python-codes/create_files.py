# coding=utf-8
# 生产40个50M大小的随机文件

import os

class CreateRandFiles:
    @staticmethod
    def create(parentPath, baseName, mbs, num):
        # 判断参数类型
        if not (isinstance(parentPath, str) and
                isinstance(baseName, str) and
                isinstance(mbs, int) and
                isinstance(num, int)):
            print '参数类型不正确'
            return
        # 创建父目录
        if not os.path.exists(parentPath):
            os.makedirs(parentPath)
        # 开始创建各个子文件
        index = 0
        while index < 40:
            fileName = parentPath + baseName + '_' + str(index)
            f = open(fileName, 'wb')
            for ii in range(1024 * mbs - 1):
                f.write(os.urandom(1024))
                f.flush()
            f.close
            index += 1
            print '已经完成 %d;' % index

def main():
    CreateRandFiles.create('c:\\tmpp\\', '50MbigFile', 50, 40)

if __name__ == '__main__':
    main()