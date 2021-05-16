def func(x):
    return x*50

def main():
    y = [2,6,8,9,5,3,4,2]
    z = map(func,y)

    for i in z:
        print(i,end=' ')



if __name__ == '__main__':
    main()