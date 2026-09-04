class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import deque
        adj = {char:set() for word in words for char in word}
        inorder = {char:0 for word in words for char in word}
        
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]

            if len(w2)<len(w1) and w1[:len(w2)] == w2:
                return ""
        
            for l1,l2 in zip(w1,w2):
                if l1 != l2:
                    if l2 not in adj[l1]:
                        adj[l1].add(l2)
                        inorder[l2] += 1
                    break
        
        queue = deque(char for char in inorder if not inorder[char])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)

            for nchar in adj[char]:
                inorder[nchar] -= 1
                
                if not inorder[nchar]:
                    queue.append(nchar)
        
        
        return "".join(res) if len(res)==len(inorder) else ""

            
        

        

                

