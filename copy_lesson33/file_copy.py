import datetime
import os
import shutil
import time
from os import path

def main():

    file = open('testfile.txt','w+')
    if path.exists('testfile.txt'):
        src = path.relpath('testfile.txt')
    head,tail = path.split(src)
    print('path: '+head)
    print('File: '+tail)

    dst = src + '.bak'
    shutil.copy(src,dst)
    shutil.copystat(src,dst)

    t = time.ctime(path.getmtime('testfile.txt.bak'))
    print(t)

    print(datetime.datetime.fromtimestamp(path.getmtime('testfile.txt.bak')))

if __name__ == '__main__':
    main()