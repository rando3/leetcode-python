'''
Created on Nov 1, 2016

@author: Prathmesh
'''
def reversecomp(dna):
    alist = []
    for x in dna:
        if x == 'a':
            alist.append('t')
        if x == 't':
            alist.append("a")
        if x == "c":
            alist.append("g")
        if x == "g":
            alist.append("c")
    alist.reverse()
    rev = ''.join(alist)
    return rev
if __name__ == '__main__':
    print reversecomp("aaggtc")