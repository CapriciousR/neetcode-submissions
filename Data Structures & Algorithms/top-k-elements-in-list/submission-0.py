class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        freq = [[] for i in range(len(nums)+1)]

        for n, c in nums_dict.items():
            freq[c].append(n)
        
        result =[]

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

                        

