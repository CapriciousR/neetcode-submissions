class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxt = []

        result = [0]*len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            while maxt and temperatures[maxt[-1]] <= temperatures[i]:
                maxt.pop()

            result[i] = maxt[-1]-i if maxt else 0

            maxt.append(i)
        
        return result