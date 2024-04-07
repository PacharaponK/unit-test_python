def alternate(s):
    alp = list(set(s))
    maxnum = count = 0

    for i in range(len(alp)):
        for j in range(i + 1, len(alp)):
            l = [alp[i], alp[j]]

            if s.index(alp[i]) < s.index(alp[j]):
                ind = 0
            else:
                ind = 1

            for char in s:
                if char in l:
                    if char == l[ind]:
                        count += 1
                        ind = ind ^ 1
                    else:
                        count = 0
                        break
            maxnum = max(maxnum, count)
            count = 0

    return maxnum
