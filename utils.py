def levenstein(str_1, str_2, w_add = 1, w_change = 1, w_del = 1):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    n, m = len(str_1), len(str_2)

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + w_add, current_row[j - 1] + w_del, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += w_change
            current_row[j] = min(add, delete, change)

    return current_row[n]