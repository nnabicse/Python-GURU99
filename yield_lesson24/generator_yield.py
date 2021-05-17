def generator():
    yield 'T'
    yield 'A'
    yield 'M'
    yield 'I'
    yield 'M'
def main():
    test = generator()
    for i in test:
        print(i)

    print(test)

if __name__ == '__main__':
    main()