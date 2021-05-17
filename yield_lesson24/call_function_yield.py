def test(x):
    return x*x
def square(x):
    for i in range(x):
        yield test(i)

def main():
    x = 10
    p = square(x)
    print(list(p))

if __name__ == '__main__':
    main()