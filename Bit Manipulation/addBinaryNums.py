def addTwoBinNums():
    a = '001'
    b = '011'
    '''
    int allows you to specify what base the first argument is in when converting from a string (in this case two), and bin converts a number back to a binary string.
    '''
    c = bin(int(a, 2) + int(b, 2))
    return c
    # 0b100


def addMultipleBinNums(*args):
    return bin(sum(int(x, 2) for x in args))[2:]  # the 2: is because first two are 0b
