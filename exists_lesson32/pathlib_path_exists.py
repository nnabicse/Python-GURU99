def main():
    import pathlib
    file = pathlib.Path('os_path_exists.py')

    if file.exists():
        print('File Exists')
    else:
        print('File not exists')

if __name__ == '__main__':
    main()