def compression(test):
    c = ''

    count = 0
    rar = 0
    z = test.count(' ')

    if z > 0:
        while ' ' in test:
            test = test.replace(' ', '')
            z = 0

    len1 = len(test)

    lst = []

    if c == '':
        newtest = test
    else:
        newtest = c
    for i in newtest:
        if newtest[newtest.index(i)] == newtest[newtest.index(i) + 1]:
            if rar != 0:
                lst.append(rar)
                count += 1
                rar = 0
            else:
                count += 1
                rar = 0

        else:
            if count != 0:
                lst.append(count)
                rar += 1
                count = 0
            else:
                rar += 1
                count = 0

    if count == 0:
        lst.append(rar)
        count = 0
        rar = 0

    else:
        lst.append(count)
        count = 0
        rar = 0

    print(newtest)

    # unpack
    print(lst)
    for item in lst:
        c += bin(item)
    c = c.replace('0b', '')
    print(c)
    len2 = len(c)
    razn = len2 * 100 / len1
    print(100 - razn)

    print(test.__sizeof__(), "Байт")
    print(c.__sizeof__(), "Байт")
    print('-----------------------------------------------------------------------------------------')


def newchange(x):
    compression(x)