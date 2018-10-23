
def summaryRange(nums):
    if nums is None:
        return None
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [str(nums[0])]

    start = nums[0]
    end = nums[0]
    ranges = []

    for i in range(1, len(nums)):
        if (nums[i] - end) == 1:
            end = nums[i]
            continue
        newRange = rangify(start, end)
        ranges.append(newRange)
        start = nums[i]
        end = nums[i]
    ranges.append(rangify(start, end))
    return ranges


def rangify(start, end):
    if start == end:
        return str(start)
    return (str(start) + "->" + str(end))


if __name__ == "__main__":
    test = [0, 1, 4, 8, 8, 8, 9, 9, 10, 11, 12, 15, 16, 16, 18, 19, 20, 20, 21, 21, 21]
    print(summaryRange(test))
