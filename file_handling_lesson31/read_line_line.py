def main():
    f = open('test.txt','r')

    f1 = f.readlines()

    for i in f1:
        print(i)


if __name__ == '__main__':
    main()