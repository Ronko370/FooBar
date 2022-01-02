stairs = {}

def substep(n, limit = 0):

    count = 0
    i = n - 1 if limit == 0 else limit

    while i > 1:
        subcount = 0
        diff = n - i
        if i <= diff:
            limit = i - 1
        else:
            limit = 0

        if (diff, limit) in stairs:
            subcount= stairs[diff, limit]
           # print(diff, substeps, curr_step, max_step)
        else:
            subcount = substep(diff, limit)

        if i > n/2:
            count += 1

        if (diff, limit) not in stairs and subcount > 0:
            stairs[diff, limit] = subcount
        count += subcount
        i -= 1
    return count

def solution(n):
    return substep(n)
