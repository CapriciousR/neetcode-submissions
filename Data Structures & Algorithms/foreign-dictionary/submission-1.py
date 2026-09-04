class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import deque,defaultdict
        adj = [[] for _ in range(26)]
        inorder = [None] * 26
        k = ord("a")

        for word in words:
            for char in word:
                inorder[ord(char)-k] = 0
        
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]

            j = 0
            while j<len(word1):
                if j>=len(word2):
                    return ""
                l1,l2 = word1[j],word2[j]

                if l1 != l2:
                    adj[ord(l1)-k].append(ord(l2)-k)
                    inorder[ord(l2)-k] += 1
                    break
                j+=1
        
        queue = deque(i for i in range(26) if inorder[i]==0)
        res = ""

        while queue:
            alpha_idx = queue.popleft()
            res += chr(alpha_idx+k)

            for nalpha_idx in adj[alpha_idx]:
                inorder[nalpha_idx] -= 1
                
                if inorder[nalpha_idx]==0:
                    queue.append(nalpha_idx)
        
        
        return res if not any(inorder) else ""

            
        

        

                

