def answer(n):
    # level 3, challenge 1
    # completed in 27 min, 8 sec
    cnt = 0
    num = long(n)
    while num != 1:
        rem = num % 4
        if rem == 0:
            num = num / 4
            cnt += 2
        elif rem == 1:
            num -= 1
            cnt += 1
            num = num / 4
            cnt += 2
        elif rem == 3:
            if num == 3:
                cnt += 2
                break
            num += 1
            cnt += 1
            num = num / 4
            cnt += 2
        else:
            cnt += 1
            num = num / 2
    print cnt


if __name__ == '__main__':
    # answer("19238410243895724839756284356347805623498523480596435892304750894235734895724389057342095872348957435982347509827509384738940732346237846314785614378561345984365918347563454763458764587136432174578745085480395734289507243059874509827458925789243752893457409857458972495862458797298752857628461")
    answer("3")
