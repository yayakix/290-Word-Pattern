class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        dict = {}
        counter = 0
        arr = []
        for x in words:
            if x not in dict:
                dict[x] = counter
            counter += 1 
        for x in words:
            arr.append(dict[x])
        # check pattern
        secdict = {}
        seccounter = 0
        secarr = []
        for x in pattern:
            if x not in secdict:
                secdict[x] = seccounter
            seccounter += 1 
        for x in pattern:
            secarr.append(secdict[x])
        return secarr == arr
