class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        def wordDiffBy1(str1,str2):
            n = len(str1)
            for i in range(len(str1)):
                if str1[i] == str2[i]:
                    n -= 1
            
            return n == 1

        visited = set([beginWord])
        
        queue = deque([beginWord])

        n_words = 0

        while queue:
            n_words += 1
            print(queue)
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return n_words

                for nword in wordList:
                    if nword not in visited and wordDiffBy1(word,nword):
                        queue.append(nword)
                        visited.add(nword)
        
        return 0
            
            

