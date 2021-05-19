def main():
    x = 'Hi myself Nurun Nabi, From East delta University'

    y = enumerate(x)

    print('Using List''\n',list(y))

    print('\nUsing For Loop: \n')

    for i in enumerate(x):
        print(i)

if __name__ == '__main__':
    main()
