def test():
    yield 'I am a good boy'

def main():
    output = test()

    for i in output:
        print(i, end='')

    print('\n',output)


if __name__ == '__main__':
    main()
