import os
import shutil
from os import path

def main():
    f = open('test1.txt','w+')
    f.close()
    if path.exists('test1.txt'):
        src = path.realpath('test1.txt')

    os.renames('test1.txt','test2.txt')
if __name__ == '__main__':
    main()