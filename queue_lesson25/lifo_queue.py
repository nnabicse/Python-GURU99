def main():
    import queue
    q1 = queue.LifoQueue(5)

    q1.put(1)
    q1.put(2)
    q1.put(3)
    q1.put(4)
    q1.put(5)

    print(q1.full())
    print(list(q1.queue))

    item1 = q1.get()

    print('Item To Remove: ',item1)

    print(list(q1.queue))

if __name__ == '__main__':
    main()