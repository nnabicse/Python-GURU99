def main():
    import queue
    q1 = queue.Queue()

    q1.put(11)
    q1.put(5)
    q1.put(4)
    q1.put(21)
    q1.put(3)
    q1.put(10)

    print(list(q1.queue))

    n = q1.qsize()

    for i in range(n):
        x = q1.get()
        print(x,end=' ')
        for j in range(n-1):
            y = q1.get()
            print(y,end=' ')
            if x>y:
                q1.put(y)
            else:
                q1.put(x)
                x=y
        q1.put(x)

    while (q1.empty() == False):
        print(q1.queue[0],end=' ')
        q1.get()

if __name__ == '__main__':
    main()