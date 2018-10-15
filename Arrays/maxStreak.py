#
# Complete the 'maxStreak' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. STRING_ARRAY data
#

def maxStreak(m, data):
    streak = 0
    for day in data:
        checkAttendance = list(day)
        if all(d == "Y" for d in checkAttendance):
            streak += 1
        else:
            return streak


if __name__ == "__main__":
    print(maxStreak(3, ["YYY", "YYY", "YYN", "YNN"]))
