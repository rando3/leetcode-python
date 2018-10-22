class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

        Like foobar, except 1.0.0 == 1.0 == 1, so have to account for that
        """
        x = [int(u) for u in version1.split(".")]
        y = [int(v) for v in version2.split(".")]
        if len(x) < len(y):
            while len(x) < len(y):
                x.append(0)  # keep zero padding until they're equal length
        if len(x) > len(y):
            while len(x) > len(y):
                y.append(0)  # keep zero padding until they're equal length

        return cmp(x, y)