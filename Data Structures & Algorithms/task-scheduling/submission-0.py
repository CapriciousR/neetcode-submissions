class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0]*26

        for task in tasks:
            cnt[ord(task)-ord("A")] += 1
        
        max_freq = max(cnt)
        z = 0
        for c in cnt:
            if c == max_freq:
                z += 1

        return max(len(tasks),(max_freq-1)*(n+1)+z)     
