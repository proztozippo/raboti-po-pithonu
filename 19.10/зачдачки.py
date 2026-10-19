while True:
    num = (int(input("введите номер, который надо проверить: ")))
    if num == 1:
        for i in range(2, 21, 2):
            print(i)

    elif num == 2:

        n = int(input(f"введите целое число: "))
        a = 0

        for i in range(n + 1):
            a += i
        print(a)

    elif num == 3:

        m, n = map(int, input("введите x1, x2 через пробел: ").split())

        if m < n:
            for i in range(m, n + 1):
                print(i)
        else:
            for i in range(m, n - 1, -1):
                print(i)

    elif num == 4:
        m, n = map(int, input("введите x1, x2 через пробел: ").split())

        for i in range(m, n):
            if m > n:
                m, n = n, m
            if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
                print(i)
            else:
                continue
    print("-" * 10)
