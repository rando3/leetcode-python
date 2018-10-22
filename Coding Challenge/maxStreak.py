#
# Complete the 'maxStreak' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. STRING_ARRAY data
#

def maxStreak(m, data):
    maxStreak = 0
    streak = 0
    for day in data:
        print(day)
        checkAttendance = list(day)
        if all(d == "Y" for d in checkAttendance):
            print("incr streak")
            streak += 1
        else:
            print("not all here")
            if streak > maxStreak:
                maxStreak = streak
                print("new max streak")
                print(maxStreak)
            streak = 0
    if streak > maxStreak:
        maxStreak = streak
    return maxStreak




if __name__ == "__main__":
    print(maxStreak(3, ["YNN", "YNN", "YYY", "YYY"]))
