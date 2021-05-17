def normal():
    return 'Hello World'

def generator():
    yield 'Hello World'

def main():
    print(normal())
    print('\n',generator())

if __name__ == '__main__':
    main()