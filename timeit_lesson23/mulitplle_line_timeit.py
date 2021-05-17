def main():
    import timeit

    print('The time is taken: ',timeit.timeit('a=10;b=10;c=a+b'))

if __name__ == '__main__':
    main()