from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        map = {}
        letters = [0 for i in range(26)]  
        for i in range(len(words)):
            for j in range(len(words[i])):
                key=ord(words[i][j])-ord('a')
                letters[key]=0
                map[key]=set()
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            idx = 0
            for j in range(min(len(word1),len(word2))):
                if(word1[j]!=word2[j]):
                    key1 = ord(word1[j])-ord('a')
                    key2 = ord(word2[j])-ord('a')
                    count = letters[key2]
                    if(key2 not in map[key1]):
                        letters[key2] =count+1
                        map[key1].add(key2)
                    break
        dictionary = collections.deque()
        res = ''
        for i in range(26):
            if(letters[i]==0 and i in map):
                dictionary.appendleft(i)
        
        while(len(dictionary)!=0):
            nextup = dictionary.pop()
            res+=(chr(nextup+ord('a')))
            greaterSet = map[nextup]
            for greater in greaterSet:
                letters[greater]-=1
                if(letters[greater]==0):
                    dictionary.appendleft(greater)
        if(len(map)!=len(res)):
            return ""
        return res

    def alienOrder1(self, words):  # topo sort BFS
        # a -> b
        adj = defaultdict(set)
        # in-degree
        deg = {c: 0 for w in words for c in w}
        for i, w1 in enumerate(words[:-1]):
            w2 = words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 == c2: continue
                if c2 not in adj[c1]: deg[c2] += 1
                adj[c1].add(c2)
                break
        res = ''
        # start w 0 indegree nodes
        q = deque([c for c in deg if not deg[c]])
        while q:
            c = q.popleft()
            res += c
            for n in adj[c]:
                deg[n] -= 1
                if not deg[n]: q.append(n)
        return res if len(res) == len(deg) else ''