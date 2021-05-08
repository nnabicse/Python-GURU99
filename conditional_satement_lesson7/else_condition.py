def main():
    x,y = 8,4

    if (x<y):
        statement = 'X is less than y'
        print(statement)
    else:
        statement = 'X is greater than y'
        print(statement)

if __name__ == '__main__':
    main()

# if there was x==y then it will also show x is greater than y
# and it is not correct. To solve this error we have to use elif
