def main():
    import os.path
    from os import path

    print('File Exists: '+str(path.exists('test.txt')))
    print('File Exists: '+str(path.exists('a.test.txt')))
    print('Directory Exists: '+str(path.exists('exists_lesson32')))

if __name__ == '__main__':
    main()