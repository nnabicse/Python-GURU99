def main():
    dict = {'x':1, 'y':2,'z':3,'d':5}

    edict = enumerate(dict)

    print('Using List: ''\n',list(edict))

    print('\n Using For Loop: \n')

    for i in enumerate(dict):
        print(i)

if __name__ == '__main__':
    main()