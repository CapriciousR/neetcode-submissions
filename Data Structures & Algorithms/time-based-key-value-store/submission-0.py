class TimeMap:

    def __init__(self):
        self.key_pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_pairs:
            self.key_pairs[key].append((timestamp,value))
        else:
            self.key_pairs[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        vals = self.key_pairs.get(key, "")
        if vals == "":
            return vals

        l,r = 0, len(vals)-1
        while l < r:
            m = (l+r+1)//2
            if vals[m][0] <= timestamp:
                l = m
            else:
                r = m-1
        
        return vals[l][1] if vals[l][0]<=timestamp else ""

