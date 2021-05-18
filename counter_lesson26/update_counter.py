def main():
    from collections import Counter

    count = Counter()

    count.update('Tamim Is a good boy with CG 3.99')

    print(count)

    count.update('ABCDEF')
    print(count)

if __name__ == '__main__':
    main()
