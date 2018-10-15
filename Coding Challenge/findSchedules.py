#
# Complete the 'findSchedules' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER workHours
#  2. INTEGER dayHours
#  3. STRING pattern
#


def findSchedules(workHours, dayHours, pattern):
    allSchedules = []
    daysToFill = 0
    hoursWorked = 0
    fillIndexes = []
    pat = list(pattern)
    for i, digit in enumerate(pat):
        if digit == "?":
            daysToFill += 1
            fillIndexes.append(i)
        else:
            hoursWorked += int(digit)

    remainingHours = workHours - hoursWorked
    if (remainingHours / dayHours) == daysToFill:
        schedule = pat[:]
        for i, v in enumerate(fillIndexes):
            schedule[v] = str(dayHours)
        s = "".join(schedule)
        allSchedules.append(s)
        return allSchedules
    hoursCombos = [[remainingHours - sum(p)] + p for p in combos(remainingHours, daysToFill - 1)]

    for combo in hoursCombos:
        valid = True
        print(combo)
        for x in combo:
            if x > dayHours:
                valid = False
        if valid:
            schedule = pat[:]
            for i, v in enumerate(fillIndexes):
                schedule[v] = str(combo[i])
            s = "".join(schedule)
            allSchedules.append(s)
    allSchedules.sort()
    return allSchedules


def combos(remHours, daysToFill, depth=0):
    if daysToFill == depth:
        return [[]]
    return [num + [i] for i in range(remHours + 1) for num in combos(remHours - i, daysToFill, depth=depth + 1)]


if __name__ == "__main__":
    # print(findSchedules(3, 1, "???????"))
    print(combos(48, 5))