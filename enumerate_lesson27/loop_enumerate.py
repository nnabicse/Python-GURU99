def main():
    x = ['a','b','c','d','e','f','g','h','i','j']

    print('\nEnumerrate Without Index: \n')

    for i in enumerate(x):
        print(i)

    print('\nEnumerrate With Index: \n')

    for i in enumerate(x,10):
        print(i)

if __name__ == '__main__':
    main()