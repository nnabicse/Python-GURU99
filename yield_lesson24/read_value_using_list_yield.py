def even(x):
    for i in range(x):
        if x%2==0:
            yield i

def main():
    n=10
    p = even(n)
    print(list(p))

if __name__ == '__main__':
    main()