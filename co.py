s = '000101111'
k = 0
for c1 in '01':
    for c2 in '01':
        for c3 in '01':
            for c4 in '01':
                for c5 in '01':
                    for c6 in '01':
                        for c7 in '01':
                            for c8 in '01':
                                for c9 in '01':
                                    tek = c1+c2+c3+c4+c5+c6+c7+c8+c9
                                    k += 1
                                    if tek == s:
                                        print(k)
                                        break
