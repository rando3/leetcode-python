import sys
# Complete the maxDifferenceOddEven function below.
def maxDifferenceOddEven(a):
    if len(a) <= 1:  # only 1 or less nums, no diff
        return -1
    max_diff = -1
    lowest_odd = sys.maxsize

    if a[0] % 2 == 1:
        lowest_odd = a[0]

    for i, num in enumerate(a[1:]):
        if num % 2 == 1:
            if num < lowest_odd:
                lowest_odd = num
            continue
        if num > lowest_odd and (num - lowest_odd) > max_diff:
            max_diff = num - lowest_odd
    return max_diff



if __name__ == "__main__":
	print(maxDifferenceOddEven([7,9,5,6,3,2]))