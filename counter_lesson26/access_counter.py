def main():
    from collections import Counter

    count = Counter()

    count.update('ABCDEFGHIABCDEF')

    print('%s:%d'%('A',count['A']))

    print('\n')

    for char in 'ABCDEFABCDE':
        print('%s:%d'%(char,count[char]))

if __name__ == '__main__':
    main()