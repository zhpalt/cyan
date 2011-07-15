# coding=utf-8

import zipfile

file = open('./data/channel.zip', 'rb')
channel = zipfile.ZipFile(file)

name = '90052.txt'
outlist = []

while name != None:
    outlist.append(channel.getinfo(name).comment.decode('ascii'))
    zipdata = channel.open(name)
    content = zipdata.read().decode('ascii')
    conlist = content.split(' ')

    #print("%s: %s" % (name, content))

    if len(conlist) == 4:
        name = conlist[3] + '.txt'
    else:
        name = None

file.close()
del channel

print(''.join(outlist))
