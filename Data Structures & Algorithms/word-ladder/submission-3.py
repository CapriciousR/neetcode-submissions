class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        from collections import deque, defaultdict
        
        adj = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])

        n_words = 0

        while queue:
            n_words += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return n_words

                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for nword in adj[pattern]:
                        if nword not in visited:
                            queue.append(nword)
                            visited.add(nword)
        
        return 0
            
            

