# a if b else c

def main():
    y: int
    x,y = 10,8

    statement = 'X is less than y' if(x<y) else 'x is greater than y'
    print(statement)

if __name__ == '__main__':
    main()