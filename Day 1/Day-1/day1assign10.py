for i in range(5):
    for j in range(0, (5-i)):
        print(end=" ")
    m = 1
    for k in range(j, 5):
        print(m, end="")
        m += 1

    n = m-2
    for k in range(5, j+1, -1):
        print(n, end="")
        n -= 1

    print()

