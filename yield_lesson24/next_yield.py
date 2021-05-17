def even(n):
    for i in range(n):
        if (i%2==0):
            yield i

def main():
    p = even(50)
    for i in p:
        print(next(p))

if __name__ == '__main__':
    main()