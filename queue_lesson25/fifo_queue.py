def main():
    import queue
    q1 = queue.Queue(5)

    q1.put(1)
    q1.put(2)
    q1.put(3)
    q1.put(4)
    q1.put(5)
    print(q1.full())

    print(list(q1.queue))

    item1 = q1.get()

    print(list(q1.queue))

    print('removed item is: ',item1)

if __name__ == '__main__':
    main()